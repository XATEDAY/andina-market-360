const filas = document.querySelector("#filas");
const estado = document.querySelector("#estado");
const filtro = document.querySelector("#producto");
const soles = new Intl.NumberFormat("es-PE", { style: "currency", currency: "PEN" });

function renderizar(datos) {
  filas.replaceChildren(...datos.map(valores => {
    const fila = document.createElement("tr");
    for (const valor of valores) {
      fila.insertCell().textContent = valor;
    }
    return fila;
  }));
}

async function cargar() {
  const respuesta = await fetch("data/resumen.json");
  if (!respuesta.ok) throw new Error("El servidor no entregó el resumen");
  const { operaciones, total, sedes, productos } = await respuesta.json();

  if (!filtro) {
    renderizar(Object.entries(productos).flatMap(([producto, totales]) =>
      Object.entries(totales).map(([sede, importe]) => [producto, sede, soles.format(importe)])
    ));
    estado.textContent = `${Object.keys(productos).length} productos`;
    return;
  }

  function actualizar() {
    const importes = filtro.value ? productos[filtro.value] : sedes;
    renderizar(Object.keys(sedes).map(sede => [sede, soles.format(importes[sede] ?? 0)]));
    estado.textContent = filtro.value
      ? `Mostrando ${filtro.value}`
      : `${operaciones} operaciones · ${soles.format(total)} en ventas`;
  }

  for (const producto of Object.keys(productos)) {
    filtro.add(new Option(producto, producto));
  }
  filtro.disabled = false;
  filtro.addEventListener("change", actualizar);
  actualizar();
}

cargar().catch(() => {
  estado.textContent = "No se pudo cargar el resumen. Genere el JSON y sirva la carpeta docs.";
});
