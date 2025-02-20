# -*- coding: utf-8 -*-
##############################################################################
#
#    Odoo ERP ,Open Source Management Solution
#    Copyright (C) 2019-2020 ISPG Technologies PVT LTD(https://www.ispg.co/)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    "name": "School Management Base",
    "version": "17.0.1.0.0",
    "author": "ISPG",
    "website": "https://www.ispg.co/",
    "category": "School Management Base",
    "license": "AGPL-3",
    "Summary": "A Module For School Management",
    "images": ["static/description/Banner_school_17.jpg"],
    "depends": [],
    "data": [
        "security/ir.model.access.csv",
        "views/student_view.xml",
    ],
    "installable": True,
    "application": True,
}
