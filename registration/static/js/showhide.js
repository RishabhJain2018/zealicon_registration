function toggleBranch(){
	if ($("#course").val()=="Btech" || $("#course").val()=="Mtech")
		$("#branch").show();
	else
		$("#branch").hide();
}
function toggleCollege(){
	if ($("#college").val()=="OTHER")
		$("#collegename").show();
	else
		$("#collegename").hide();
}

$(document).ready(function(){
	$("#course").change(function(){
		toggleBranch();
	});
	$("#college").change(function(){
		toggleCollege();	
	});

 // $("#college").autocomplete({
 //    source:'/college_auto_complete/' ,
 //    minLength: 1,
 //  });

});
// $(function(){
// 	var availableColleges=[
// 	"JSS Academy of Technical Education",
// 	"Jaypee Institute of Information & Technology",
// 	"IIT Madras",
// 	"IIT Indore",
// 	 ]
//   $("#college").autocomplete({
//     source: availableColleges ,
//     minLength: 1,
//   });
// });