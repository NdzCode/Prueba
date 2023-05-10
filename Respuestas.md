

### Evaluacion 

**Nombre:** Nicolas Vega
**Profesor:** 
**Asignatura**

---

1.  Indique los comandos para crear subir la version del proyecto git a un       repositorio remoto.

- Respuesta los pasos son:

1. git init
2. git add [Nombre de archivo]
3. git commit -m "Comentario"
4. git remote add origin main " URL"
5. git push -v origin main
---
2.  ¿Como se puede utilizar el codigo de un proyecto git en un repositorio remoto
(github) en un computador local

- Respuesta los pasos son los siguientes :

- Clonar el repositorio, a local: **git clone [URL]**, permite descargar el codeigo del repositorio remoto a local 


---

3. Si se implementa un codigo en python que crea un objeto de una clase abstracta,
¿Que sucede al ejecutar dicho codigo?

- Respuesta: si se ejecuta dicha clase la terminal lanzara error, para ejecutar esta se debe dar comom argumento a otra clase ej 

'' 

   

    class operacion(ABC):
        pass 

    class Herramienta(operacion):
            pass              
 
--- 

4.  ¿Que significa que un metodo tenga el decorador @abstractmethod
- Respuesta:
    Esto permite declarar que el metodo sera Abstracto

---


5.  Indique 3 eventos que pueden ejecutarse en una interfaz grafica de usuario.

- Respuesta: 

    **.clicked.connec(self.metodo)**

    **mousePressEvent(self, e):**

    **mouseReleaseEvent(self, e):**

---

6.  ¿Que es el ciclo de eventos?

    El ciclo de eventos, captura todos los eventos constantemente, si el evento esta ligado a **metodos** o  **clases**, este ejecuta y vuelve a capturar eventos, **(hay eventos que cierran la ejecucion del programa y se detiene el ciclo de eventos)**

---

7.  Si desde la ventana principal de un prograna se lanza un objeto de clase QDialog

¿Es posible ignorarlo y seguir utilizando la ventana principal?

- Respuesta:

    No. para seguir utilizando la ventana principal es necesario ocuparse primero de la ventana emergente para continuar con la ventana principal

8. Mencione al menos 5 componentes graficos de PyQt6

- Respuesta:

    1.  **Qlabel()**

    2. **QLineEdit()**

    3. **QTextEdit()**
    
    4. **QPushButton()**

    5. **QHBoxLayout()**


9. Si se requiere de ingresar datos numeticos, que alternativas existen de componentes
en PyQt6

- Respuesta:

        1.  QLineEdit() # catura texto, luego utilizamos una metodo que lo trasforme int float


10.  ¿Como es posible utilizar una interfaz creada con Qt Designer en un codigo fuente
en python con PyQt6?

        

