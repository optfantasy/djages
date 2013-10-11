from django.conf import settings

class GlobalAPIException(Exception):
    def __init__(self, code, debug=None):
        self.code = code
        self.debug = debug

ERROR_GENERAL_NO_ERROR                  = 00000 #: No error
ERROR_GENERAL_UNKNOWN_ERROR             = 10000 #: Last ditch error, unkown cause
ERROR_GENERAL_BAD_SIGNATURE             = 10001 #: Request parameters don't match method signature
ERROR_GENERAL_NOT_FOUND                 = 10002 #: Resource does not exist
ERROR_GENERAL_USER_NOT_FOUND            = 10003 #: User does not exist
ERROR_GENERAL_BAD_TYPE                  = 10004 #: Content type does not exist
ERROR_GENERAL_TARGET_NOT_FOUND          = 10005 #: Target object not found
ERROR_GENERAL_BAD_ID_FORMAT             = 10006 #: Bad ID format
ERROR_GENERAL_INVALID_OPERATION         = 10007 #: Not effective operation (already done or not allowed)
ERROR_GENERAL_BAD_PARA_FORMAT           = 10008 #: Some requested parameters are not valid
ERROR_AUTH_NOT_AUTHENTICATED            = 10100 #: Requested authenticated resource anonymously
ERROR_AUTH_BAD_CREDENTIALS              = 10101 #: Bad username/password combo
ERROR_AUTH_NOT_AUTHORIZED               = 10102 #: Not authorized resource access
ERROR_AUTH_PASSWORD_CONFIRM_NOT_MATCH   = 10103 #: Passwords do not match.
ERROR_AUTH_NO_PASSWORD                  = 10104 #: No password
ERROR_AUTH_PASSWORD_INVALID             = 10105 #: The password should be between 6 to 20 characters
ERROR_AUTH_USER_ALREADY_LOGIN           = 10106 #: User already log in
ERROR_AUTH_USER_ALREADY_ACTIVATED       = 10107 #: User have already been activated
ERROR_AUTH_USER_CANNT_CHANGE_USERNAME   = 10108 #: User can't change username anymore
ERROR_AUTH_USER_EMAIL_NOT_EXIST         = 10109 #: Email does not exist
ERROR_AUTH_USER_NO_GROUP                = 10110 #: User have to create group before logging in
ERROR_AUTH_PASSWORD_CONFIRM_INVALID     = 10111 #: The confirmation password should be between 6 to 20 characters
ERROR_AUTH_USERNAME_NOT_EXIST           = 10112 #: The username you entered does not exist
ERROR_USER_PASSWORD_NOT_MATCH           = 10200 #: Incorrect password
ERROR_USER_FREIND_REQUEST_NOT_FOUND     = 10201 #: Friend request is not found
ERROR_USER_INVALID_FEEDBACK             = 10202 #: Feedback cannot be empty

API_ERRORS = {
    ERROR_GENERAL_NO_ERROR: "No Error.",
    ERROR_GENERAL_UNKNOWN_ERROR: "Unknown error.  Please contact API team.",
    ERROR_GENERAL_BAD_SIGNATURE: "Method signature does not match.",
    ERROR_GENERAL_NOT_FOUND: "Page not found.",
    ERROR_GENERAL_USER_NOT_FOUND: "User could not be found.",
    ERROR_GENERAL_BAD_TYPE: "Content type is invalid or does not exist.",
    ERROR_GENERAL_TARGET_NOT_FOUND: "Target object does not exist.",
    ERROR_GENERAL_BAD_ID_FORMAT : "Bad ID format.",
    ERROR_GENERAL_INVALID_OPERATION : "Not effective operation (already done or not allowed).",
    ERROR_GENERAL_BAD_PARA_FORMAT : "Some requested parameters are not valid.",
    ERROR_AUTH_NOT_AUTHENTICATED: "Authentication required.",
    ERROR_AUTH_BAD_CREDENTIALS: "Invalid username/password combination.",
    ERROR_AUTH_NOT_AUTHORIZED: "The request user is not authorized to access this resource.",
    ERROR_AUTH_PASSWORD_CONFIRM_NOT_MATCH: "Passwords do not match.",
    ERROR_AUTH_NO_PASSWORD: "Password should not be empty.",
    ERROR_AUTH_PASSWORD_INVALID: "The password should be between 6 to 20 characters.",
    ERROR_AUTH_USER_ALREADY_LOGIN: "User have already logged in.",
    ERROR_AUTH_USER_ALREADY_ACTIVATED: "User have already been activated.",
    ERROR_AUTH_USER_CANNT_CHANGE_USERNAME: "User can't change username anymore.",
    ERROR_AUTH_USER_EMAIL_NOT_EXIST: "Email does not exist.",
    ERROR_AUTH_USER_NO_GROUP: "You have to create group before logging in",
    ERROR_AUTH_PASSWORD_CONFIRM_INVALID: "The confirmation password should be between 6 to 20 characters.",
    ERROR_AUTH_USERNAME_NOT_EXIST: "The username you entered does not exist",
    ERROR_USER_PASSWORD_NOT_MATCH: "Incorrect password.",
    ERROR_USER_FREIND_REQUEST_NOT_FOUND : "Friend request is not found",
    ERROR_USER_INVALID_FEEDBACK : "Feedback cannot be empty",
}
