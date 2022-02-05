var form_elements = document.getElementsByClassName('form-element');
var info_elements = document.getElementsByClassName('info-element');
var editbtn = document.getElementById('editbtn');
var pdfbtn = document.getElementById('pdfbtn');
var backbtn = document.getElementById('backbtn');

backbtn.style.display = 'none';

for(var i = 0;i<form_elements.length;i++){
    form_elements[i].style.display = 'none';
}

const showForm = () => {
    editbtn.style.display = 'none';
    pdfbtn.style.display = 'none';
    backbtn.style.display = 'block';
    for(var i = 0;i<form_elements.length;i++){
        form_elements[i].style.display = 'block';
    }
    for(var i = 0;i<info_elements.length;i++){
        info_elements[i].style.display = 'none';
    }
}

function delback(){
    backbtn.style.display = 'none';
}