function sayHello() {
    eel.say_hello_py("HTML");  // Llama a la función de Python
}



// Función para cerrar la aplicación Python al cerrar la ventana
window.onbeforeunload = function() {
    eel.setCycleFalse();
    eel.close();
};


$(document).ready(function() {
    $("#start_rainbow_mode").click(function() {
        eel.start_rainbow_cycle();
    });
    $("#stop_rainbow_mode").click(function() {
        eel.stop_rainbow_cycle();
    });
});
