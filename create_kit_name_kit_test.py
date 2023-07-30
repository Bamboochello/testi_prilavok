import data
import sender_stand_request


def get_user_token():
    response = sender_stand_request.post_new_user(data.user_body)
    return response.json()["authToken"]

def get_kit_headers(auth_token):
    current_headers = data.headers.copy()
    current_headers["Authorization"] = "Bearer " + auth_token
    return current_headers

def get_kit_body(name):
    current_body = data.kit_body.copy()
    current_body["name"] = name
    return current_body

def positive_assert(name):
    auth_token = get_user_token()
    kit_body = get_kit_body(name)
    kit_headers = get_kit_headers(auth_token)
    user_response = sender_stand_request.post_new_user_kit(kit_body, kit_headers)
    assert user_response.status_code == 201

def test_create_kit_1_letter_in_name_get_success_response():
    positive_assert("a")

def test_create_kit_511_letter_in_name_get_success_response():
    positive_assert("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC")

def test_create_kit_has_eng_letter_in_name_get_success_response():
    positive_assert("QWErty")

def test_create_kit_has_ru_letter_in_name_get_success_response():
    positive_assert("Мария")

def test_create_kit_has_special_symbol_in_name_get_success_response():
    positive_assert("\"№%@\",")

def test_create_kit_has_space_in_name_get_success_response():
    positive_assert(" Человек и КО ")

def test_create_kit_has_numbers_in_name_get_success_response():
    positive_assert("123")

def negative_assert_symbol(name):
    auth_token = get_user_token()
    kit_body = get_kit_body(name)
    kit_headers = get_kit_headers(auth_token)
    user_response = sender_stand_request.post_new_user_kit(kit_body, kit_headers)
    assert user_response.status_code == 400

def negative_assert_no_name(kit_body):
    auth_token = get_user_token()
    kit_headers = get_kit_headers(auth_token)
    response = sender_stand_request.post_new_user_kit(kit_body, kit_headers)
    assert response.status_code == 400

def test_negative_assert_empty_name_get_error_response():
    kit_body = get_kit_body("")
    negative_assert_symbol(kit_body)

def test_create_kit_512_letter_in_name_get_error_response():
    negative_assert_symbol("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD")

def test_create_user_no_name_get_error_response():
    kit_body = data.kit_body.copy()
    kit_body.pop("name")
    negative_assert_no_name(kit_body)

def test_negative_assert_use_invalid_type_name_get_error_response():
    kit_body = get_kit_body(123)
    negative_assert_symbol(kit_body)
