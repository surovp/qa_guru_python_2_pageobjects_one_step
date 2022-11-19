from selene import have
from selene.support.shared import browser


#Функция, которая, среди всех элементов из переменной element, найдёт тот элемент, у которого текст = option
def select_radiobutton_gender(element, gender):
    browser.all(element).element_by(have.exact_text(gender)).click()

