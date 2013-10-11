from piston.emitters import Emitter
from api.emitters import GuluEmitter
Emitter.unregister('json')
Emitter.register('json', GuluEmitter, 'application/json; charset=utf-8')