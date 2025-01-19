class Urls:
    URL = 'https://stellarburgers.nomoreparties.site'


class Endpoint:
    CREATE_USER = Urls.URL + '/api/auth/register'
    LOGIN_USER = Urls.URL + '/api/auth/login'
    UPD_USER_INFO = Urls.URL + '/api/auth/user'
    CREATE_ORDER = Urls.URL + '/api/orders'
    ORDER_LIST = Urls.URL + '/api/orders'
    DELETE_USER = Urls.URL + "/api/auth/user"


class StatusCodes:
    OK = 200
    CREATED = 201
    ACCEPTED = 202
    BAD_REQUEST = 400
    UNAUTHORIZED = 401
    FORBIDDEN = 403
    NOT_FOUND = 404
    CONFLICT = 409
    ERROR_500 = 500


class IngredientsHush:
    BUN = "61c0c5a71d1f82001bdaaa6c"
    SAUCE = "61c0c5a71d1f82001bdaaa72"
    MAIN = "61c0c5a71d1f82001bdaaa70"
