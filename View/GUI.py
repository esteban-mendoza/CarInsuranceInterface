from tkinter import *
from tkinter import ttk
from View.Datepicker import Datepicker


class GUI(ttk.Frame):

    def __init__(self, master):
        # Main frame
        super().__init__(master, padding="3 3 12 12")
        super().grid(row=0, column=0, sticky=(N, W, E, S))

        # Master settings
        master.title("Pólizas")
        master.columnconfigure(0, weight=1)
        master.rowconfigure(0, weight=1)

        # Cliente
        self.lf_cliente = ttk.Labelframe(self, text="Cliente")
        self.lf_cliente.grid(row=0, column=0, rowspan=3, columnspan=6)

        self.val_id_cliente = BooleanVar()
        self.ch_id_cliente = ttk.Checkbutton(self.lf_cliente, variable=self.val_id_cliente)
        self.ch_id_cliente.grid(row=1, column=0)

        self.la_id_cliente = ttk.Label(self.lf_cliente, text="id_cliente")
        self.la_id_cliente.grid(row=1, column=1)

        self.id_cliente = StringVar()
        self.en_id_cliente = ttk.Entry(self.lf_cliente, width=14, textvariable=self.id_cliente)
        self.en_id_cliente.grid(row=1, column=2)

        self.val_nombre = BooleanVar()
        self.ch_nombre = ttk.Checkbutton(self.lf_cliente, variable=self.val_nombre)
        self.ch_nombre.grid(row=1, column=3)

        self.la_nombre = ttk.Label(self.lf_cliente, text="Nombre")
        self.la_nombre.grid(row=1, column=4)

        self.nombre = StringVar()
        self.en_nombre = ttk.Entry(self.lf_cliente, width=40, textvariable=self.nombre)
        self.en_nombre.grid(row=1, column=5)

        self.val_direccion = BooleanVar()
        self.ch_direccion = ttk.Checkbutton(self.lf_cliente, variable=self.val_direccion)
        self.ch_direccion.grid(row=2, column=0)

        self.la_direccion = ttk.Label(self.lf_cliente, text="Dirección")
        self.la_direccion.grid(row=2, column=1)

        self.direccion = StringVar()
        self.en_direccion = ttk.Entry(self.lf_cliente, width=75, textvariable=self.direccion)
        self.en_direccion.grid(row=2, column=2, columnspan=4)

        for child in self.lf_cliente.winfo_children():
            child.grid_configure(padx=5, pady=5)

        # Factura
        self.lf_factura = ttk.LabelFrame(self, text="Factura")
        self.lf_factura.grid(row=0, column=6, rowspan=3, columnspan=3)

        self.val_id_factura = BooleanVar()
        self.ch_id_factura = ttk.Checkbutton(self.lf_factura, variable=self.val_id_factura)
        self.ch_id_factura.grid(row=1, column=6)

        self.la_id_factura = ttk.Label(self.lf_factura, text="id_factura")
        self.la_id_factura.grid(row=1, column=7)

        self.id_factura = StringVar()
        self.en_id_factura = ttk.Entry(self.lf_factura, width=14, textvariable=self.id_factura)
        self.en_id_factura.grid(row=1, column=8)

        self.val_costo_auto = BooleanVar()
        self.ch_costo_auto = ttk.Checkbutton(self.lf_factura, variable=self.val_costo_auto)
        self.ch_costo_auto.grid(row=2, column=6)

        self.la_costo_auto = ttk.Label(self.lf_factura, text="Costo del\nautomóvil")
        self.la_costo_auto.grid(row=2, column=7)

        self.costo_auto = StringVar()
        self.en_costo_auto = ttk.Entry(self.lf_factura, width=14, textvariable=self.costo_auto)
        self.en_costo_auto.grid(row=2, column=8)

        for child in self.lf_factura.winfo_children():
            child.grid_configure(padx=5, pady=5)

        # Vehículo
        self.lf_vehiculo = ttk.LabelFrame(self, text="Vehículo")
        self.lf_vehiculo.grid(row=3, column=6, rowspan=4, columnspan=3)

        self.val_placas = BooleanVar()
        self.ch_placas = ttk.Checkbutton(self.lf_vehiculo, variable=self.val_placas)
        self.ch_placas.grid(row=4, column=0)

        self.la_placas = ttk.Label(self.lf_vehiculo, text="Placas")
        self.la_placas.grid(row=4, column=1)

        self.placas = StringVar()
        self.en_placas = ttk.Entry(self.lf_vehiculo, width=14, textvariable=self.placas)
        self.en_placas.grid(row=4, column=2)

        self.val_marca = BooleanVar()
        self.ch_marca = ttk.Checkbutton(self.lf_vehiculo, variable=self.val_marca)
        self.ch_marca.grid(row=5, column=0)

        self.la_marca = ttk.Label(self.lf_vehiculo, text="Marca")
        self.la_marca.grid(row=5, column=1)

        self.marca = StringVar()
        self.en_marca = ttk.Entry(self.lf_vehiculo, width=14, textvariable=self.marca)
        self.en_marca.grid(row=5, column=2)

        self.val_modelo = BooleanVar()
        self.ch_modelo = ttk.Checkbutton(self.lf_vehiculo, variable=self.val_modelo)
        self.ch_modelo.grid(row=6, column=0)

        self.la_modelo = ttk.Label(self.lf_vehiculo, text="Modelo")
        self.la_modelo.grid(row=6, column=1)

        self.modelo = StringVar()
        self.en_modelo = ttk.Entry(self.lf_vehiculo, width=14, textvariable=self.modelo)
        self.en_modelo.grid(row=6, column=2)

        for child in self.lf_vehiculo.winfo_children():
            child.grid_configure(padx=5, pady=5)

        # Póliza
        self.lf_poliza = ttk.LabelFrame(self, text="Póliza")
        self.lf_poliza.grid(row=3, column=0, rowspan=3, columnspan=6)

        self.val_costo_seguro = BooleanVar()
        self.ch_costo_seguro = ttk.Checkbutton(self.lf_poliza, variable=self.val_costo_seguro)
        self.ch_costo_seguro.grid(row=4, column=3)

        self.la_costo_seguro = ttk.Label(self.lf_poliza, text="Costo del\nseguro")
        self.la_costo_seguro.grid(row=4, column=4)

        self.costo_seguro = StringVar()
        self.en_costo_seguro = ttk.Entry(self.lf_poliza, width=14, textvariable=self.costo_seguro)
        self.en_costo_seguro.grid(row=4, column=5)

        self.val_poliza = BooleanVar()
        self.ch_poliza = ttk.Checkbutton(self.lf_poliza, variable=self.val_poliza)
        self.ch_poliza.grid(row=5, column=3)

        self.la_poliza = ttk.Label(self.lf_poliza, text="Póliza")
        self.la_poliza.grid(row=5, column=4)

        self.poliza = StringVar()
        self.en_poliza = ttk.Entry(self.lf_poliza, width=14, textvariable=self.poliza)
        self.en_poliza.grid(row=5, column=5)

        self.val_apertura = BooleanVar()
        self.ch_apertura = ttk.Checkbutton(self.lf_poliza, variable=self.val_apertura)
        self.ch_apertura.grid(row=4, column=6)

        self.la_apertura = ttk.Label(self.lf_poliza, text="Fecha de\napertura")
        self.la_apertura.grid(row=4, column=7)

        self.apertura = StringVar()
        self.en_apertura = Datepicker(self.lf_poliza, datevar=self.apertura)
        self.en_apertura.grid(row=4, column=8)

        self.val_vencimiento = BooleanVar()
        self.ch_vencimiento = ttk.Checkbutton(self.lf_poliza, variable=self.val_vencimiento)
        self.ch_vencimiento.grid(row=5, column=6)

        self.la_vencimiento = ttk.Label(self.lf_poliza, text="Fecha de\nvencimiento")
        self.la_vencimiento.grid(row=5, column=7)

        self.vencimiento = StringVar()
        self.en_vencimiento = Datepicker(self.lf_poliza, datevar=self.vencimiento)
        self.en_vencimiento.grid(row=5, column=8)

        for child in self.lf_poliza.winfo_children():
            child.grid_configure(padx=5, pady=5)

        # Table
        self.tabla = ttk.Treeview(self, selectmode=BROWSE)
        self.tabla.grid(row=7, column=0, rowspan=7, columnspan=8, sticky=W+E+N+S)

        # Scroll bars
        self.vscroll = ttk.Scrollbar(self, orient=VERTICAL)
        self.vscroll.grid(row=7, column=8, rowspan=7, sticky=W+N+S)

        self.hscroll = ttk.Scrollbar(self, orient=HORIZONTAL)
        self.hscroll.grid(row=14, column=0, columnspan=8, sticky=W+E+N)

        # Scroll bars binding
        self.vscroll.configure(command=self.tabla.yview)
        self.hscroll.configure(command=self.tabla.xview)

        self.tabla.configure(yscrollcommand=self.vscroll.set)
        self.tabla.configure(xscrollcommand=self.hscroll.set)

        # Buttons
        self.bo_mostrar = ttk.Button(self, text="Mostrar todo", width=16)
        self.bo_mostrar.grid(row=7, column=9, sticky=W)

        self.bo_buscar = ttk.Button(self, text="Buscar", width=16)
        self.bo_buscar.grid(row=8, column=9, sticky=W)

        self.bo_actualizar = ttk.Button(self, text="Actualizar", width=16)
        self.bo_actualizar.grid(row=9, column=9, sticky=W)

        self.bo_eliminar = ttk.Button(self, text="Eliminar", width=16)
        self.bo_eliminar.grid(row=10, column=9, sticky=W)

        # Padding of elements in self
        for child in self.winfo_children():
            child.grid_configure(padx=5, pady=5)


if __name__ == '__main__':
    root = Tk()
    GUI(root)
    root.mainloop()
