var form_elements = document.getElementsByClassName('form-element');
var info_elements = document.getElementsByClassName('info-element');

for(var i = 0;i<form_elements.length;i++){
    form_elements[i].style.display = 'none';
}

const showForm = () => {
    for(var i = 0;i<form_elements.length;i++){
        form_elements[i].style.display = 'block';
    }
    for(var i = 0;i<info_elements.length;i++){
        info_elements[i].style.display = 'none';
    }
}