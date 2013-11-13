#!/bin/bash
export SED="sed"
while [ $# -gt 0 ]
do
    case "$1" in
        -b) branch=`echo "$2" | sed 's/\./\\\./g'`; shift;;
        --web_ip)
            web_ip=`echo "$2" | sed 's/\./\\\./g'`;
            shift;;
        --mongo_ips)
            mongo_ips=`echo "$2" | sed 's/\./\\\./g' | sed 's/#/\,/g'`;
            shift;;
        -*) echo >&2 \
            "usage: $0 [-b branch] [--web_ip ip] [--mongo_ips]"
            exit 1;;
        *)  break;;
    esac
    shift
done

for IP_LABEL in web_ip mongo_ips
do
    if [ "${!IP_LABEL}" == "" ]; then
        echo "--${IP_LABEL} is required!"
        break;
    fi
    echo "$IP_LABEL => ${!IP_LABEL}"
    echo "nginx"
    sed -i "s/$IP_LABEL/${!IP_LABEL}/g" /home/djages/site/djages/repository/djages/configs/staging/nginx
    echo "apache"
    sed -i "s/$IP_LABEL/${!IP_LABEL}/g" /home/djages/site/djages/repository/djages/configs/staging/apache
    echo "settings.py"
    sed -i "s/$IP_LABEL/${!IP_LABEL}/g" /home/djages/site/djages/repository/djages/configs/staging/settings.py
done

echo "cp nginx/apache configuration to site-enabled"
cd /home/djages/site/djages/repository
sudo cp djages/configs/staging/nginx /etc/nginx/sites-enabled/djages

sudo cp djages/configs/staging/apache /etc/apache2/sites-enabled/djages
sudo cp djages/configs/staging/ports.conf /etc/apache2/
# sudo cp djages/configs/staging/proxy.conf /etc/nginx/proxy.conf

echo "virtual env activate"
cd /home/djages/site/djages/repository
. ../env/bin/activate

echo "remove statics"
rm -rf ./djages/static/*
cd ./djages/configs/staging
echo "collect static"
python manage.py collectstatic --noinput --verbosity=0

#echo "comlile less files"
#cd /home/djages/site/djages/repository/djages/static
#lessc -x ./less/base.less > ./css/base.css

echo "restart apache2"
sudo /etc/init.d/apache2 restart
echo "done"
echo "restart nginx"
sudo /etc/init.d/nginx restart
echo "done"

