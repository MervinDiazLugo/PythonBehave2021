import logging
import allure
from allure_commons.types import AttachmentType
from selenium import webdriver
from behave import fixture
from functions.Functions import Functions as Selenium
from functions.Inicializar import Inicializar


def before_all(self):
    pass


def before_feature(self, feature):
    pass


def before_scenario(self, scenario):
    if "FIREFOX" in scenario.tags:
        self.driver = Selenium.abrir_navegador(self, navegador="FIREFOX")
    else:
        self.driver = Selenium.abrir_navegador(self)

    if Inicializar.Environment == 'Dev':
        Inicializar.Scenario["Udemy"] = "Hola Chicos Dev"

    if Inicializar.Environment == 'Test':
        Inicializar.Scenario["Udemy"] = "Hola Chicos Test"


def before_step(self, step):
    pass


def before_tag(self, tag):
    pass


def after_all(self):
    pass


def after_feature(self, feature):
    pass


def after_scenario(self, scenario):
    Selenium.tearDown(self)


def after_step(self, step):
    pass






