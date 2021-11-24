# <?xml version="1.0" encoding="utf-8"?>
# <odoo>
#
#     <record id="action_confirm_appointments" model="ir.actions.server">
#         <field name="name">Confirm Appointment</field>
#         <field name="type">ir.actions.server</field>
#         <field name="model_id" ref="model_hospital_appointment"/>
#         <field name="binding_model_id" ref="model_hospital_appointment"/>
#         <field name="state">code</field>
#         <field name="code">records.action_confirm()</field>
#     </record>
#
#     <record id="view_appointment_tree" model="ir.ui.view">
#         <field name="name">hospital.appointment.tree</field>
#         <field name="model">hospital.appointment</field>
#         <field name="arch" type="xml">
#             <tree multi_edit="1">
#                 <header>
#                     <button name="action_done" string="Mark As Done" class="btn-primary"
#                             type="object"/>
#                 </header>
#                 <field name="name"/>
#                 <field name="doctor_id"/>
#                 <field name="patient_id"/>
#                 <field name="age" optional="show"/>
#                 <field name="gender" optional="show"/>
#                 <field name="date_appointment" optional="show"/>
#                 <field name="date_checkup" optional="hide"/>
#                 <field name="note" optional="show"/>
#                 <field name="state" optional="show"/>
#             </tree>
#         </field>
#     </record>
#
#     <record id="view_appointment_form" model="ir.ui.view">
#         <field name="name">hospital.appointment.form</field>
#         <field name="model">hospital.appointment</field>
#         <field name="arch" type="xml">
#             <form>
#                 <header>
#                     <button id="button_confirm" name="action_confirm" string="Confirm" class="btn-primary" states="draft"
#                             confirm="Are you sure that you need to confirm ?"
#                             type="object"/>
#                     <button id="button_done" name="action_done" string="Mark As Done" class="btn-primary" states="confirm"
#                             type="object"/>
#                     <button id="button_draft" name="action_draft" string="Set To Draft" class="btn-primary"
#                             states="cancel" type="object"/>
#                     <button id="button_cancel" name="action_cancel" string="Cancel" states="draft,done,confirm"
#                             confirm="Are you sure that you need to cancel ?"
#                             type="object"/>
#                     <button name="action_url" string="Open URL" class="btn-primary"
#                             type="object"/>
#                     <field name="state" widget="statusbar" statusbar_visible="draft,done,confirm"/>
#                 </header>
#                 <sheet>
#                     <div class="oe_title">
#                         <h1>
#                             <field name="name" readonly="1"/>
#                         </h1>
#                     </div>
#                     <group>
#                         <group>
#                             <field name="patient_id"/>
#                             <field name="gender" readonly="1" force_save="1"/>
#                             <field name="age"/>
#                         </group>
#                         <group>
#                             <field name="doctor_id"/>
#                             <field name="date_appointment"/>
#                             <field name="date_checkup"/>
#                         </group>
#                     </group>
#                     <notebook>
#                         <page string="Doctor Prescription" name="doctor_prescription">
#                             <group>
#                                 <field name="prescription"/>
#                             </group>
#                         </page>
#                         <page string="Medicine" name="medicine">
#                             <field name="prescription_line_ids">
#                                 <tree editable="bottom">
#                                     <field name="name"/>
#                                     <field name="qty"/>
#                                 </tree>
#                                 <form>
#                                     <group>
#                                         <group>
#                                             <field name="name"/>
#                                         </group>
#                                         <group>
#                                             <field name="qty"/>
#                                         </group>
#                                     </group>
#                                 </form>
#                             </field>
#                         </page>
#                         <page string="Other Info" name="other_info">
#                             <field name="note"/>
#                         </page>
#                     </notebook>
#                 </sheet>
#                 <div class="oe_chatter">
#                     <field name="message_follower_ids"/>
#                     <field name="activity_ids"/>
#                     <field name="message_ids"/>
#                 </div>
#             </form>
#         </field>
#     </record>
#
#     <record id="view_appointment_search" model="ir.ui.view">
#         <field name="name">hospital.appointment.search</field>
#         <field name="model">hospital.appointment</field>
#         <field name="arch" type="xml">
#             <search string="Patients">
#                 <field name="name"/>
#                 <field name="patient_id"/>
#                 <separator/>
#                 <filter string="Draft" name="draft" domain="[('state', '=', 'draft')]"/>
#                 <group expand="1" string="Group By">
#                     <filter string="Patient" name="patient_id" context="{'group_by':'patient_id'}"/>
#                 </group>
#             </search>
#         </field>
#     </record>
#
#     <record id="action_hospital_appointment" model="ir.actions.act_window">
#         <field name="name">Appointments</field>
#         <field name="type">ir.actions.act_window</field>
#         <field name="res_model">hospital.appointment</field>
#         <field name="view_mode">tree,form</field>
#         <field name="context">{'search_default_draft': 1}</field>
#         <field name="help" type="html">
#             <p class="o_view_nocontent_smiling_face">
#                 Create your first appointment !
#             </p>
#         </field>
#     </record>
#
#     <menuitem id="menu_appointment_root"
#               name="Appointments"
#               parent="menu_hospital_root"
#               sequence="20"/>
#
#     <menuitem id="menu_appointment"
#               name="Appointments"
#               parent="menu_appointment_root"
#               action="action_hospital_appointment"
#               sequence="10"/>
#
#     <menuitem id="menu_create_appointment"
#               name="Create Appointment"
#               parent="menu_appointment_root"
#               action="action_create_appointment"
#               sequence="20"/>
#
#     <menuitem id="menu_search_appointment"
#               name="Search Appointment"
#               parent="menu_appointment_root"
#               action="action_search_appointment"
#               sequence="30"/>
#
# </odoo>