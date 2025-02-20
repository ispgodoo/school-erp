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

from odoo import _, api, fields, models

class StudentStudent(models.Model):
    """Defining a student information."""

    _name = "student.student"
    _description = "Student Information"
    name = fields.Char(string="Name",required="1")
    date_of_birth = fields.Date(
        "BirthDate",
        required=True,
        help="Enter student date of birth",
    )
   


