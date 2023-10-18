# -*- coding: utf-8 -*-
{
    'name': 'employee_hide_work_permit',
    'summary': 'Employee hide work permit',
    'description': 'Employee hide work permit',

    'author': 'Volodymyr Dziadyk',
    'website': 'https://www.oneservice-consulting.com/',
    'support': 'dvol@oneservice.in.ua',

    'category': 'Human Resources/Employees',
    'license': 'LGPL-3',
    'version': '16.0.1.0.1',

    'depends': [
        'base',
    ],

    'data': [
        'security/ir.model.access.csv'
        'views/views.xml',
     ],
    'demo': [
    ],

    'application': False,
    'installable': True,
    'auto_install': False,

}
