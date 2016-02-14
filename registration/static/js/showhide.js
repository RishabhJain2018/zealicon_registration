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

});

