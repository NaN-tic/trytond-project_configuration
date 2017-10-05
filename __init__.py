# This file is part project_configuration module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.pool import Pool
from . import configuration


def register():
    Pool.register(
        configuration.Configuration,
        module='project_configuration', type_='model')
