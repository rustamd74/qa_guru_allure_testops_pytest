import allure


@allure.id("16143")
@allure.title("Auth via Google(clone)")
@allure.tag("web", "smoke")
@allure.story("External Auth")
@allure.feature("Auth")
@allure.label("msrv", "Auth")
@allure.label("owner", "allure8")
def test_google_auth():
    with allure.step("Открыть главную страницу"):
        pass
    with allure.step("Выбирать способ авторизации через Google"):
        pass
    with allure.step("Авторизоваться как пользователь JohnDoe"):
        with allure.step("Ввести логин johndoe@gmail.com"):
            pass
    with allure.step("Ввести пароль 123456789"):
        pass
    with allure.step("Нажать на кнопку Войти"):
        pass
    with allure.step("Проверить успешную авторизацию"):
        pass
    with allure.step("Проверить обновление данных из Google"):
        with allure.step("Имя: JohnDoe"):
            pass
    with allure.step("Email: johndoe@gmail.com"):
        pass
