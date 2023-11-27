# Python_3ra_entrega
Para la presente entrega se ha creado un portal de clientes destinado a la administración de ventas y la gestión del negocio. Por tal motivo el desarrollo de la página web,
se realizó teniendo en cuenta como usuario final al administrador de una unidad comercial.

En el proyecto que se presenta a continuación pueden identificarse por un lado las funciones destinadas a almacenar información en la base de datos, mientras que el otro grupo se encarga de mostrar dicha información por pantalla.

Las funciones que almacenan información consisten en formularios web que el usuario deberá completar con los datos solicitados y que se desean ingresar. Entre estas tenemos:

Agregar cliente: Se accede desde /app/clientes/ y permite dar de alta clientes de la empresa. Los campos a completar son 'Nombre', 'Dni', 'Email'. Si la empresa es una persona jurídica se debe poner aquí la
clave tributaria o análoga.

Agregar producto:Se accede desde /app/productos/ y permite la carga de 'Id producto', 'Nombre producto' y 'Precio venta' de cada producto que se desee agregar al listado de artículos disponibles para la venta.

Agregar venta: Se accede desde /app/ventas/ y permite cargar las ventas realizadas. Los campos a completar son 'Dni' del cliente al cual le vendimos, 'Nombre producto' que se vendió y ' Cantidad vendida'

Por otra parte el segundo grupo de funciones que se encarga de mostrar la información almacenada en la base de datos se compone de:

Clientes: Se accede desde /app/mostrar_clientes/ Muestra por pantalla el nombre, número de documento y correo electrónico de cada cliente ingresado por la empresa. Además admite la opción de BÚSQUEDA por el Dni del cliente.

Productos: Se accede desde /app/mostrar_productos/ y muestra el nombre del producto, su ID y su precio de venta de cada producto, uno debajo del otro.

Ventas: Se accede desde /app/mostrar_ventas/ y muestra las ventas realizadas, es decir: nombre del producto vendido, DNI del cliente y cantidad de esos objetos vendidos en la misma transacción a ese cliente.

