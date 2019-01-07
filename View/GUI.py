from tkinter import *
from tkinter import ttk
from View.Datepicker import Datepicker
from Controller.Controller import Controller
from tkinter.filedialog import askopenfilename

"""
Autor: Jorge Esteban Mendoza Ortiz (418002863)
Email: esteban.mendoza@ciencias.unam.mx
"""


class GUI(ttk.Frame):
    fields_current_query = dict()

    def __init__(self, master):
        self.control = Controller()

        # Main frame
        super().__init__(master)
        super().grid(row=0, column=0, sticky=(N, W, E, S))

        # Master settings
        master.title("Pólizas")
        master.columnconfigure(0, weight=1)
        master.rowconfigure(0, weight=1)

        # Notebook
        self.notebook = ttk.Notebook(self, padding=10)
        self.notebook.grid(row=0, column=0, sticky=(N, W, E, S))

        # Consultas frame
        self.fr_consultas = ttk.Frame(self.notebook)
        self.notebook.add(self.fr_consultas, text="Consultas", padding=10)

        # Agregar registros / importar frame
        self.fr_agregar = ttk.Frame(self.notebook)
        self.notebook.add(self.fr_agregar, text="Agregar / Importar", padding=10)

        # Ayuda frame
        self.fr_ayuda = ttk.Frame(self.notebook)
        self.notebook.add(self.fr_ayuda, text="Ayuda", padding=10)

        # Cliente
        self.lf_cliente = ttk.Labelframe(self.fr_consultas, text="Cliente")
        self.lf_cliente.grid(row=0, column=0, rowspan=3, columnspan=6)

        self.val_id_cliente = BooleanVar()
        self.ch_id_cliente = ttk.Checkbutton(self.lf_cliente, variable=self.val_id_cliente)
        self.ch_id_cliente.grid(row=1, column=0)

        self.la_id_cliente = ttk.Label(self.lf_cliente, text="id_cliente")
        self.la_id_cliente.grid(row=1, column=1)

        self.id_cliente = StringVar()
        self.en_id_cliente = ttk.Entry(self.lf_cliente,  textvariable=self.id_cliente)
        self.en_id_cliente.grid(row=1, column=2)

        self.val_nombre = BooleanVar()
        self.ch_nombre = ttk.Checkbutton(self.lf_cliente, variable=self.val_nombre)
        self.ch_nombre.grid(row=1, column=3)

        self.la_nombre = ttk.Label(self.lf_cliente, text="Nombre")
        self.la_nombre.grid(row=1, column=4)

        self.nombre = StringVar()
        self.en_nombre = ttk.Entry(self.lf_cliente, width=34, textvariable=self.nombre)
        self.en_nombre.grid(row=1, column=5)

        self.val_direccion = BooleanVar()
        self.ch_direccion = ttk.Checkbutton(self.lf_cliente, variable=self.val_direccion)
        self.ch_direccion.grid(row=2, column=0)

        self.la_direccion = ttk.Label(self.lf_cliente, text="Dirección")
        self.la_direccion.grid(row=2, column=1)

        self.direccion = StringVar()
        self.en_direccion = ttk.Entry(self.lf_cliente, width=72, textvariable=self.direccion)
        self.en_direccion.grid(row=2, column=2, columnspan=4)

        for child in self.lf_cliente.winfo_children():
            child.grid_configure(padx=5, pady=5)

        # Factura
        self.lf_factura = ttk.LabelFrame(self.fr_consultas, text="Factura")
        self.lf_factura.grid(row=0, column=6, rowspan=3, columnspan=3)

        self.val_id_factura = BooleanVar()
        self.ch_id_factura = ttk.Checkbutton(self.lf_factura, variable=self.val_id_factura)
        self.ch_id_factura.grid(row=1, column=6)

        self.la_id_factura = ttk.Label(self.lf_factura, text="id_factura")
        self.la_id_factura.grid(row=1, column=7)

        self.id_factura = StringVar()
        self.en_id_factura = ttk.Entry(self.lf_factura,  textvariable=self.id_factura)
        self.en_id_factura.grid(row=1, column=8)

        self.val_costo_vehiculo = BooleanVar()
        self.ch_costo_vehiculo = ttk.Checkbutton(self.lf_factura, variable=self.val_costo_vehiculo)
        self.ch_costo_vehiculo.grid(row=2, column=6)

        self.la_costo_vehiculo = ttk.Label(self.lf_factura, text="Costo del\nautomóvil")
        self.la_costo_vehiculo.grid(row=2, column=7)

        self.costo_vehiculo = StringVar()
        self.en_costo_vehiculo = ttk.Entry(self.lf_factura,  textvariable=self.costo_vehiculo)
        self.en_costo_vehiculo.grid(row=2, column=8)

        for child in self.lf_factura.winfo_children():
            child.grid_configure(padx=5, pady=5)

        # Vehículo
        self.lf_vehiculo = ttk.LabelFrame(self.fr_consultas, text="Vehículo")
        self.lf_vehiculo.grid(row=3, column=6, rowspan=4, columnspan=3)

        self.val_placas = BooleanVar()
        self.ch_placas = ttk.Checkbutton(self.lf_vehiculo, variable=self.val_placas)
        self.ch_placas.grid(row=4, column=0)

        self.la_placas = ttk.Label(self.lf_vehiculo, text="Placas")
        self.la_placas.grid(row=4, column=1)

        self.placas = StringVar()
        self.en_placas = ttk.Entry(self.lf_vehiculo,  textvariable=self.placas)
        self.en_placas.grid(row=4, column=2)

        self.val_marca = BooleanVar()
        self.ch_marca = ttk.Checkbutton(self.lf_vehiculo, variable=self.val_marca)
        self.ch_marca.grid(row=5, column=0)

        self.la_marca = ttk.Label(self.lf_vehiculo, text="Marca")
        self.la_marca.grid(row=5, column=1)

        self.marca = StringVar()
        self.en_marca = ttk.Entry(self.lf_vehiculo,  textvariable=self.marca)
        self.en_marca.grid(row=5, column=2)

        self.val_modelo = BooleanVar()
        self.ch_modelo = ttk.Checkbutton(self.lf_vehiculo, variable=self.val_modelo)
        self.ch_modelo.grid(row=6, column=0)

        self.la_modelo = ttk.Label(self.lf_vehiculo, text="Modelo")
        self.la_modelo.grid(row=6, column=1)

        self.modelo = StringVar()
        self.en_modelo = ttk.Entry(self.lf_vehiculo,  textvariable=self.modelo)
        self.en_modelo.grid(row=6, column=2)

        for child in self.lf_vehiculo.winfo_children():
            child.grid_configure(padx=5, pady=5)

        # Póliza
        self.lf_poliza = ttk.LabelFrame(self.fr_consultas, text="Póliza")
        self.lf_poliza.grid(row=3, column=0, rowspan=3, columnspan=6)

        self.val_costo_seguro = BooleanVar()
        self.ch_costo_seguro = ttk.Checkbutton(self.lf_poliza, variable=self.val_costo_seguro)
        self.ch_costo_seguro.grid(row=4, column=3)

        self.la_costo_seguro = ttk.Label(self.lf_poliza, text="Costo del\nseguro")
        self.la_costo_seguro.grid(row=4, column=4)

        self.costo_seguro = StringVar()
        self.en_costo_seguro = ttk.Entry(self.lf_poliza,  textvariable=self.costo_seguro)
        self.en_costo_seguro.grid(row=4, column=5)

        self.val_prima_asegurada = BooleanVar()
        self.ch_prima_asegurada = ttk.Checkbutton(self.lf_poliza, variable=self.val_prima_asegurada)
        self.ch_prima_asegurada.grid(row=5, column=3)

        self.la_prima_asegurada = ttk.Label(self.lf_poliza, text="Prima asegurada")
        self.la_prima_asegurada.grid(row=5, column=4)

        self.prima_asegurada = StringVar()
        self.en_prima_asegurada = ttk.Entry(self.lf_poliza,  textvariable=self.prima_asegurada)
        self.en_prima_asegurada.grid(row=5, column=5)

        self.val_fecha_apertura = BooleanVar()
        self.ch_fecha_apertura = ttk.Checkbutton(self.lf_poliza, variable=self.val_fecha_apertura)
        self.ch_fecha_apertura.grid(row=4, column=6)

        self.la_fecha_apertura = ttk.Label(self.lf_poliza, text="Fecha de\napertura")
        self.la_fecha_apertura.grid(row=4, column=7)

        self.fecha_apertura = StringVar()
        self.en_fecha_apertura = Datepicker(self.lf_poliza, datevar=self.fecha_apertura)
        self.en_fecha_apertura.grid(row=4, column=8)

        self.val_fecha_vencimiento = BooleanVar()
        self.ch_fecha_vencimiento = ttk.Checkbutton(self.lf_poliza, variable=self.val_fecha_vencimiento)
        self.ch_fecha_vencimiento.grid(row=5, column=6)

        self.la_fecha_vencimiento = ttk.Label(self.lf_poliza, text="Fecha de\nvencimiento")
        self.la_fecha_vencimiento.grid(row=5, column=7)

        self.fecha_vencimiento = StringVar()
        self.en_fecha_vencimiento = Datepicker(self.lf_poliza, datevar=self.fecha_vencimiento)
        self.en_fecha_vencimiento.grid(row=5, column=8)

        for child in self.lf_poliza.winfo_children():
            child.grid_configure(padx=5, pady=5)

        # Table
        self.fr_tabla = ttk.Frame(self.fr_consultas, width=900, height=180)
        self.fr_tabla.grid(row=7, column=0, rowspan=8, columnspan=10)
        self.fr_tabla.grid_propagate(0)

        self.tabla = ttk.Treeview(self.fr_tabla, height=12, selectmode=BROWSE)
        self.tabla.grid(row=7, column=0, sticky=N+S+W+E)
        self.tabla.bind("<<TreeviewSelect>>", self.populate_fields)

        # Scroll bars
        self.vscroll = ttk.Scrollbar(self.fr_tabla, orient=VERTICAL)
        self.vscroll.grid(row=7, column=9, rowspan=7, sticky=W+N+S)

        self.hscroll = ttk.Scrollbar(self.fr_tabla, orient=HORIZONTAL)
        self.hscroll.grid(row=14, column=0, columnspan=9, sticky=W+E+N)

        # Scroll bars binding
        self.vscroll.configure(command=self.tabla.yview)
        self.hscroll.configure(command=self.tabla.xview)

        self.tabla.configure(yscrollcommand=self.vscroll.set)
        self.tabla.configure(xscrollcommand=self.hscroll.set)

        # Buttons
        self.bo_mostrar = ttk.Button(self.fr_consultas, text="Mostrar todo", width=16,
                                     command=self.show_all)
        self.bo_mostrar.grid(row=1, column=9, sticky=W)

        self.bo_limpiar = ttk.Button(self.fr_consultas, text="Limpiar campos", width=16)
        self.bo_limpiar.grid(row=2, column=9, sticky=W)

        self.bo_buscar = ttk.Button(self.fr_consultas, text="Buscar", width=16)
        self.bo_buscar.grid(row=3, column=9, sticky=W)

        self.bo_actualizar = ttk.Button(self.fr_consultas, text="Actualizar", width=16)
        self.bo_actualizar.grid(row=4, column=9, sticky=W)

        self.bo_eliminar = ttk.Button(self.fr_consultas, text="Eliminar", width=16)
        self.bo_eliminar.grid(row=5, column=9, sticky=W)

        # Padding of elements in consultas frame
        for child in self.fr_consultas.winfo_children():
            child.grid_configure(padx=5, pady=5)

        # Ayuda frame widgets
        self.la_ayuda = ttk.Label(self.fr_ayuda,
                                  text="Licenciatura en Matemáticas Aplicadas\n\n"
                                       "Proyecto final para la materia de Manejo de Datos.\n"
                                       "Profesor: M. en C. Miguel Ángel Pérez León\n\n"
                                       "Autor: Jorge Esteban Mendoza Ortiz (418002863)\n")
        self.la_ayuda.grid(row=0, column=0)

        # Padding of elements in ayuda frame
        for child in self.fr_ayuda.winfo_children():
            child.grid_configure(padx=5, pady=5)

        # Agregar / importar frame widgets
        self.la_instruccion = ttk.Label(self.fr_agregar,
                                        text="NOTA: \n"
                                             "Los campos marcados con * no pueden estar vacíos.\n"
                                             "Los campos marcados con + pueden dejarse en blanco y se generan "
                                             "automáticamente.")
        self.la_instruccion.grid(row=0, column=0, pady=20)

        self.lf_ag_cliente = ttk.Labelframe(self.fr_agregar, text="Cliente")
        self.lf_ag_cliente.grid(row=4, column=0, rowspan=3, columnspan=8, sticky=(E, W))

        self.la_ag_id_cliente = ttk.Label(self.lf_ag_cliente, text="id_cliente+")
        self.la_ag_id_cliente.grid(row=1, column=1)

        self.ag_id_cliente = StringVar()
        self.en_ag_id_cliente = ttk.Entry(self.lf_ag_cliente, textvariable=self.ag_id_cliente)
        self.en_ag_id_cliente.grid(row=1, column=2)

        self.la_ag_nombre = ttk.Label(self.lf_ag_cliente, text="Nombre")
        self.la_ag_nombre.grid(row=1, column=4)

        self.ag_nombre = StringVar()
        self.en_ag_nombre = ttk.Entry(self.lf_ag_cliente, width=35, textvariable=self.ag_nombre)
        self.en_ag_nombre.grid(row=1, column=5)

        self.la_ag_direccion = ttk.Label(self.lf_ag_cliente, text="Dirección")
        self.la_ag_direccion.grid(row=2, column=1)

        self.ag_direccion = StringVar()
        self.en_ag_direccion = ttk.Entry(self.lf_ag_cliente, width=68, textvariable=self.ag_direccion)
        self.en_ag_direccion.grid(row=2, column=2, columnspan=4)

        self.bo_ag_cliente = ttk.Button(self.lf_ag_cliente, width=18,
                                        text="Agregar cliente", command=self.insert_cliente)
        self.bo_ag_cliente.grid(row=1, column=6)

        self.bo_importar_clientes = ttk.Button(self.lf_ag_cliente, width=18,
                                               text="Importar clientes", command=self.importar_clientes)
        self.bo_importar_clientes.grid(row=2, column=6)

        for child in self.lf_ag_cliente.winfo_children():
            child.grid_configure(padx=5, pady=5)

        self.lf_ag_vehiculo = ttk.Labelframe(self.fr_agregar, text="Vehículo")
        self.lf_ag_vehiculo.grid(row=7, column=0, rowspan=3, columnspan=8, sticky=(E, W))

        self.la_ag_placas = ttk.Label(self.lf_ag_vehiculo, text="Placas*")
        self.la_ag_placas.grid(row=1, column=1)

        self.ag_placas = StringVar()
        self.en_ag_placas = ttk.Entry(self.lf_ag_vehiculo, textvariable=self.ag_placas)
        self.en_ag_placas.grid(row=1, column=2)

        self.la_ag_id_factura = ttk.Label(self.lf_ag_vehiculo, text="id_factura")
        self.la_ag_id_factura.grid(row=2, column=1)

        self.ag_id_factura = StringVar()
        self.en_ag_id_factura = ttk.Entry(self.lf_ag_vehiculo, textvariable=self.ag_id_factura)
        self.en_ag_id_factura.grid(row=2, column=2)

        self.la_ag_marca = ttk.Label(self.lf_ag_vehiculo, text="Marca")
        self.la_ag_marca.grid(row=1, column=3)

        self.ag_marca = StringVar()
        self.en_ag_marca = ttk.Entry(self.lf_ag_vehiculo, textvariable=self.ag_marca)
        self.en_ag_marca.grid(row=1, column=4)

        self.la_ag_modelo = ttk.Label(self.lf_ag_vehiculo, text="Modelo")
        self.la_ag_modelo.grid(row=2, column=3)

        self.ag_modelo = StringVar()
        self.en_ag_modelo = ttk.Entry(self.lf_ag_vehiculo, textvariable=self.ag_modelo)
        self.en_ag_modelo.grid(row=2, column=4)

        self.bo_ag_vehiculo = ttk.Button(self.lf_ag_vehiculo, width=18,
                                         text="Agregar vehículo", command=self.insert_vehiculo)
        self.bo_ag_vehiculo.grid(row=1, column=6)

        self.bo_importar_vehiculo = ttk.Button(self.lf_ag_vehiculo, width=18,
                                               text="Importar vehículos")
        self.bo_importar_vehiculo.grid(row=2, column=6)

        for child in self.lf_ag_vehiculo.winfo_children():
            child.grid_configure(padx=5, pady=5)

        self.lf_ag_factura = ttk.Labelframe(self.fr_agregar, text="Factura")
        self.lf_ag_factura.grid(row=10, column=0, rowspan=3, columnspan=8, sticky=(E, W))

        self.la_ag_id_factura2 = ttk.Label(self.lf_ag_factura, text="id_factura+")
        self.la_ag_id_factura2.grid(row=1, column=1)

        self.ag_id_factura2 = StringVar()
        self.en_ag_id_factura2 = ttk.Entry(self.lf_ag_factura, textvariable=self.ag_id_factura2)
        self.en_ag_id_factura2.grid(row=1, column=2)

        self.la_ag_placas2 = ttk.Label(self.lf_ag_factura, text="Placas*")
        self.la_ag_placas2.grid(row=2, column=1)

        self.ag_placas2 = StringVar()
        self.en_ag_placas2 = ttk.Entry(self.lf_ag_factura, textvariable=self.ag_placas2)
        self.en_ag_placas2.grid(row=2, column=2)

        self.la_ag_costo = ttk.Label(self.lf_ag_factura, text="Costo del vehículo*")
        self.la_ag_costo.grid(row=1, column=3)

        self.ag_costo = StringVar()
        self.en_ag_costo = ttk.Entry(self.lf_ag_factura, textvariable=self.ag_costo)
        self.en_ag_costo.grid(row=1, column=4)

        self.bo_ag_factura = ttk.Button(self.lf_ag_factura, width=18,
                                        text="Agregar factura", command=self.insert_factura)
        self.bo_ag_factura.grid(row=1, column=5)

        self.bo_importar_facturas = ttk.Button(self.lf_ag_factura, width=18,
                                               text="Importar facturas")
        self.bo_importar_facturas.grid(row=2, column=5)

        for child in self.lf_ag_factura.winfo_children():
            child.grid_configure(padx=5, pady=5)

        self.lf_ag_poliza = ttk.Labelframe(self.fr_agregar, text="Póliza")
        self.lf_ag_poliza.grid(row=1, column=0, rowspan=3, columnspan=8, sticky=(E, W))

        self.la_ag_id_cliente2 = ttk.Label(self.lf_ag_poliza, text="id_cliente*")
        self.la_ag_id_cliente2.grid(row=1, column=1)

        self.ag_id_cliente2 = StringVar()
        self.en_ag_id_cliente2 = ttk.Entry(self.lf_ag_poliza, textvariable=self.ag_id_cliente2)
        self.en_ag_id_cliente2.grid(row=1, column=2)

        self.la_ag_id_factura3 = ttk.Label(self.lf_ag_poliza, text="id_factura*")
        self.la_ag_id_factura3.grid(row=2, column=1)

        self.ag_id_factura3 = StringVar()
        self.en_ag_id_factura3 = ttk.Entry(self.lf_ag_poliza, textvariable=self.ag_id_factura3)
        self.en_ag_id_factura3.grid(row=2, column=2)

        self.la_ag_costo_seguro = ttk.Label(self.lf_ag_poliza, text="Costo del seguro+")
        self.la_ag_costo_seguro.grid(row=1, column=3)

        self.ag_costo_seguro = StringVar()
        self.en_ag_costo_seguro = ttk.Entry(self.lf_ag_poliza, textvariable=self.ag_costo_seguro)
        self.en_ag_costo_seguro.grid(row=1, column=4)

        self.la_ag_prima = ttk.Label(self.lf_ag_poliza, text="Prima asegurada+")
        self.la_ag_prima.grid(row=2, column=3)

        self.ag_prima = StringVar()
        self.en_ag_prima = ttk.Entry(self.lf_ag_poliza, textvariable=self.ag_prima)
        self.en_ag_prima.grid(row=2, column=4)

        self.la_ag_apertura = ttk.Label(self.lf_ag_poliza, text="Fecha de apertura+")
        self.la_ag_apertura.grid(row=1, column=5)

        self.ag_apertura = StringVar()
        self.en_ag_apertura = Datepicker(self.lf_ag_poliza, datevar=self.ag_apertura)
        self.en_ag_apertura.grid(row=1, column=6)

        self.la_ag_vencimiento = ttk.Label(self.lf_ag_poliza, text="Fecha de vencimiento+")
        self.la_ag_vencimiento.grid(row=2, column=5)

        self.ag_vencimiento = StringVar()
        self.en_ag_vencimiento = Datepicker(self.lf_ag_poliza, datevar=self.ag_vencimiento)
        self.en_ag_vencimiento .grid(row=2, column=6)

        self.bo_gen_poliza = ttk.Button(self.lf_ag_poliza, width=18,
                                        text="Generar póliza", command=self.gen_poliza)
        self.bo_gen_poliza.grid(row=1, column=7)

        for child in self.lf_ag_poliza.winfo_children():
            child.grid_configure(padx=5, pady=5)

        # Padding of elements in agregar / importar frame
        for child in self.fr_agregar.winfo_children():
            child.grid_configure(padx=5, pady=5)

    def insert_cliente(self):
        data = dict()
        if self.ag_id_cliente.get():
            data['id_cliente'] = int(self.ag_id_cliente.get())
        if self.ag_nombre.get():
            data['nombre'] = self.ag_nombre.get()
        if self.ag_direccion.get():
            data['direccion'] = self.ag_direccion.get()
        self.control.insert_cliente(**data)

    def insert_vehiculo(self):
        data = dict()
        if self.ag_placas.get():
            data['placas'] = self.ag_placas.get()
        if self.ag_id_factura.get():
            data['id_factura'] = int(self.ag_id_factura.get())
        if self.ag_marca.get():
            data['marca'] = self.ag_marca.get()
        if self.ag_modelo.get():
            data['modelo'] = self.ag_modelo.get()
        self.control.insert_vehiculo(**data)

    def insert_factura(self):
        data = dict()
        if self.ag_id_factura2.get():
            data['id_factura'] = int(self.ag_id_factura2.get())
        if self.ag_placas2.get():
            data['placas'] = self.ag_placas2.get()
        if self.ag_costo.get():
            data['costo_vehiculo'] = float(self.ag_costo.get())
        self.control.insert_factura(**data)

    def gen_poliza(self):
        data = dict()
        if self.ag_id_cliente2.get():
            data['id_cliente'] = int(self.ag_id_cliente2.get())
        if self.ag_id_factura3.get():
            data['id_factura'] = int(self.ag_id_factura3.get())
        if self.ag_prima.get():
            data['prima_asegurada'] = float(self.ag_prima.get())
        if self.ag_costo_seguro.get():
            data['costo_seguro'] = float(self.ag_costo_seguro.get())
        if self.ag_apertura.get():
            data['fecha_apertura'] = self.ag_apertura.get()
        if self.ag_vencimiento.get():
            data['fecha_vencimiento'] = self.ag_vencimiento.get()
        self.control.gen_poliza(**data)

    def importar_clientes(self):
        path = askopenfilename()
        self.control.insert_clientes(path)

    def importar_vehiculos(self):
        path = askopenfilename()
        self.control.insert_vehiculos(path)

    def importar_facturas(self):
        path = askopenfilename()
        self.control.insert_facturas(path)

    def get_active_fields(self):
        active_fields = dict()

        active_fields["id_cliente"] = self.val_id_cliente.get()
        active_fields["nombre"] = self.val_nombre.get()
        active_fields["direccion"] = self.val_direccion.get()
        active_fields["placas"] = self.val_placas.get()
        active_fields["marca"] = self.val_marca.get()
        active_fields["modelo"] = self.val_modelo.get()
        active_fields["id_factura"] = self.val_id_factura.get()
        active_fields["costo_vehiculo"] = self.val_costo_vehiculo.get()
        active_fields["prima_asegurada"] = self.val_prima_asegurada.get()
        active_fields["costo_seguro"] = self.val_costo_seguro.get()
        active_fields["fecha_apertura"] = self.val_fecha_apertura.get()
        active_fields["fecha_vencimiento"] = self.val_fecha_vencimiento.get()

        return active_fields

    def show_all(self):
        self.clear_results()

        # Set columnas
        all_fields = {
            # Clientes
            "id_cliente": True,
            "nombre": True,
            "direccion": True,
            # Facturas
            "id_factura": True,
            "costo_vehiculo": True,
            # Pólizas
            "costo_seguro": True,
            "prima_asegurada": True,
            "fecha_apertura": True,
            "fecha_vencimiento": True,
            # Vehículos
            "placas": True,
            "marca": True,
            "modelo": True
        }
        self.set_columnas(all_fields)
        self.fields_current_query = all_fields

        # Query
        self.control.query_all(all_fields)

        # Agregar filas
        for i, row in enumerate(self.control.connection.cursor):
            self.tabla.insert("", END, text=str(i+1), values=row)

    def set_columnas(self, fields):
        # Set columns
        self.tabla.configure(columns=tuple(fields))
        for column in fields.keys():
            self.tabla.column(column, width=15)

        # Set headings
        self.tabla.heading("#0", text="No.")
        if fields.get("id_cliente", False):
            self.tabla.heading("id_cliente", text="id_cliente")
        if fields.get("nombre", False):
            self.tabla.heading("nombre", text="Nombre")
        if fields.get("direccion", False):
            self.tabla.heading("direccion", text="Dirección")
        if fields.get("placas", False):
            self.tabla.heading("placas", text="Placas")
        if fields.get("modelo", False):
            self.tabla.heading("modelo", text="Modelo")
        if fields.get("marca", False):
            self.tabla.heading("marca", text="Marca")
        if fields.get("id_factura", False):
            self.tabla.heading("id_factura", text="id_factura")
        if fields.get("costo_vehiculo", False):
            self.tabla.heading("costo_vehiculo", text="Costo del vehículo")
        if fields.get("prima_asegurada", False):
            self.tabla.heading("prima_asegurada", text="Prima asegurada")
        if fields.get("costo_seguro", False):
            self.tabla.heading("costo_seguro", text="Costo del seguro")
        if fields.get("fecha_apertura", False):
            self.tabla.heading("fecha_apertura", text="Fecha de apertura")
        if fields.get("fecha_vencimiento", False):
            self.tabla.heading("fecha_vencimiento", text="Fecha de vencimiento")

    def clear_results(self):
        for child in self.tabla.get_children():
            self.tabla.delete(child)

    def populate_fields(self, e):
        row_id = self.tabla.selection()[0]

        if self.fields_current_query["id_cliente"]:
            self.id_cliente.set(str(self.tabla.set(row_id, "id_cliente")))
        if self.fields_current_query["nombre"]:
            self.nombre.set(str(self.tabla.set(row_id, "nombre")))
        if self.fields_current_query["direccion"]:
            self.direccion.set(str(self.tabla.set(row_id, "direccion")))
        if self.fields_current_query["placas"]:
            self.placas.set(str(self.tabla.set(row_id, "placas")))
        if self.fields_current_query["marca"]:
            self.marca.set(str(self.tabla.set(row_id, "marca")))
        if self.fields_current_query["modelo"]:
            self.modelo.set(str(self.tabla.set(row_id, "modelo")))
        if self.fields_current_query["id_factura"]:
            self.id_factura.set(str(self.tabla.set(row_id, "id_factura")))
        if self.fields_current_query["costo_vehiculo"]:
            self.costo_vehiculo.set(str(self.tabla.set(row_id, "costo_vehiculo")))
        if self.fields_current_query["prima_asegurada"]:
            self.prima_asegurada.set(str(self.tabla.set(row_id, "prima_asegurada")))
        if self.fields_current_query["costo_seguro"]:
            self.costo_seguro.set(str(self.tabla.set(row_id, "costo_seguro")))
        if self.fields_current_query["fecha_apertura"]:
            self.fecha_apertura.set(str(self.tabla.set(row_id, "fecha_apertura")))
        if self.fields_current_query["fecha_vencimiento"]:
            self.fecha_vencimiento.set(str(self.tabla.set(row_id, "fecha_vencimiento")))



if __name__ == '__main__':
    root = Tk()
    GUI(root)
    root.mainloop()
