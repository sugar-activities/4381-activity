#! /usr/bin/env python
"Emulador de Visual Boy Advance y Game Boy Advance                                           Christofer Roibal                                                    yyaaeell@hotmail.com                                                                    CeibalJam  http://ceibaljam.org"

from sugar.activity import activity
import sys, os, subprocess
import gtk, gobject
import logging

from sugar.graphics.toolbutton import ToolButton
from sugar.graphics.toolbarbox import ToolbarBox
from sugar.graphics.toolbarbox import ToolbarButton

from sugar.activity.widgets import ActivityToolbarButton

from helpbutton import HelpButton

class JamGBA(activity.Activity):

	def __init__(self, handle):

		activity.Activity.__init__(self, handle)

        	self.max_participants = 1

        	toolbar_box = ToolbarBox()

        	activity_button = ActivityToolbarButton(self)
        	toolbar_box.toolbar.insert(activity_button, 0)
        	activity_button.show()

		jugarc_button = ToolButton('chico')
		jugarc_button.set_tooltip(('Jugar el juego en pantalla chica'))
		jugarc_button.connect('clicked', self._jugar_chico)
		toolbar_box.toolbar.insert(jugarc_button, -1)
		jugarc_button.show

		jugarm_button = ToolButton('mediano')
		jugarm_button.set_tooltip(('Jugar el juego en pantalla mediana'))
		jugarm_button.connect('clicked', self._jugar_mediano)
		toolbar_box.toolbar.insert(jugarm_button, -1)
		jugarm_button.show

		jugarg_button = ToolButton('grande')
		jugarg_button.set_tooltip(('Jugar el juego en pantalla grande'))
		jugarg_button.connect('clicked', self._jugar_grande)
		toolbar_box.toolbar.insert(jugarg_button, -1)
		jugarg_button.show
		
        	separator = gtk.SeparatorToolItem()
        	separator.props.draw = False
        	separator.set_expand(True)
        	toolbar_box.toolbar.insert(separator, -1)
        	separator.show()

       	 	self.create_help(toolbar_box.toolbar)

       		self.set_toolbar_box(toolbar_box)
        	toolbar_box.show()
        	self._update_accelerators(toolbar_box)

		self._filechooser = gtk.FileChooserWidget(\
		action=gtk.FILE_CHOOSER_ACTION_OPEN,backend=None)
		self._filechooser.set_current_folder("/")
		self.botonJugar = gtk.Button("Jugar rom")
		self.botonJugar.connect('clicked', self._jugar_mediano)
		self.botonJugar.show ()
		self._filechooser.set_extra_widget(self.botonJugar)
		self.set_canvas(self._filechooser)
		self.show_all()


	def _jugar_chico(self, widget, data=None):

		archivo = self._filechooser.get_filename()
		#socket = gtk.Socket()
		#socket.show()
		#self.set_canvas(socket)
		#self.show_all()

		#xid=socket.get_id()


		romopen = [ "bin/vba", "-2", archivo]
                subprocess.Popen(romopen)

	def _jugar_mediano(self, widget, data=None):

		archivo = self._filechooser.get_filename()
		#socket = gtk.Socket()
		#socket.show()
		#self.set_canvas(socket)
		#self.show_all()

		#xid=socket.get_id()


		romopen = [ "bin/vba", "-3", archivo]
                subprocess.Popen(romopen)

	def _jugar_grande(self, widget, data=None):

		archivo = self._filechooser.get_filename()
		#socket = gtk.Socket()
		#socket.show()
		#self.set_canvas(socket)
		#self.show_all()

		#xid=socket.get_id()


		romopen = [ "bin/vba", "-4", archivo]
                subprocess.Popen(romopen)


	def __become_root_cb(self, button):
		os.popen("gedit")

    	def _update_accelerators(self, container):
            for child in container.get_children():
                if isinstance(child, ToolButton):
                    if child.props.accelerator is not None:
                        # This code is copied from toolbutton.py
                        # to solve workaround bug described in OLPC #10930
                        accel_group = self.get_data('sugar-accel-group')
                        keyval, mask = gtk.accelerator_parse(
                                                    child.props.accelerator)
                        # the accelerator needs to be set at the child,
                        # so the gtk.AccelLabel
                        # in the palette can pick it up.
                        child.child.add_accelerator('clicked', accel_group,
                                    keyval, mask,
                                    gtk.ACCEL_LOCKED | gtk.ACCEL_VISIBLE)

                if isinstance(child, ToolbarButton):
                    if child.get_page() is not None:
                         self._update_accelerators(child.get_page())
                if hasattr(child, 'get_children'):
                     self._update_accelerators(child)

	def create_help(self, toolbar):
            helpitem = HelpButton()
            toolbar.insert(helpitem, -5)
            helpitem.show()
            helpitem.add_paragraph(('Para abrir un juego busca el juego el el directorio donde lo descargastes o guardastes, dale click arriba y luego dale click a unos de los botones de la barra para poder jugarlo o dale click en donde dice jugar rom en la parte de abajo'))
            helpitem.add_paragraph(('Este boton abre el juego en una pantalla chica'), 'chico')
            helpitem.add_paragraph(('Este boton abre el juego en una pantalla mediana'), 'mediano')
            helpitem.add_paragraph(('Este boton abre el juego en una pantalla grande'), 'grande')
	    helpitem.add_paragraph(('Para salir del juego  apreta las teclas Control+Q o pon en el marco el puntero sobre el icono de la actividad y da click en Parar'))
