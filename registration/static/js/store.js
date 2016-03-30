window.onload = function() {

  if(localStorage){
    console.log(localStorage)
    var name= localStorage.getItem('name')
    var email= localStorage.getItem('email')
    var course= localStorage.getItem('course')
    var branch= localStorage.getItem('branch1')
    var contact= localStorage.getItem('contact')
    var college= localStorage.getItem('college')
    var year= localStorage.getItem('year')

    document.getElementById('name').value=name;
    document.getElementById('email').value=email
    document.getElementById('course').value=course
    document.getElementById('branch1').value=branch
    document.getElementById('contact').value=contact
    document.getElementById('college').value=college
    document.getElementById('year').value=year

    document.getElementById('registerform').addEventListener('submit',function(){
      var name = document.getElementById('name').value;
      var email = document.getElementById('email').value;
      var course = document.getElementById('course').value;
      var branch = document.getElementById('branch1').value;
      var contact = document.getElementById('contact').value;
      var college = document.getElementById('college').value;
      var year = document.getElementById('year').value;

      localStorage.setItem('name',name);
      localStorage.setItem('email',email);
      localStorage.setItem('course',course);
      localStorage.setItem('branch1',branch);
      localStorage.setItem('contact',contact);
      localStorage.setItem('college',college);
      localStorage.setItem('year',year);


    });
  }
}