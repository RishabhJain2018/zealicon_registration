function toggleBranch(){
	if ($("#course").val()=="Btech")
		$("#branch").show();
	else
		$("#branch").hide();
}
function toggleCollege(){
	if ($("#college").val()=="JSS")
		$("#collegename").hide();
	else
		$("#collegename").show();
}

$(document).ready(function(){
	$("#course").change(function(){
		toggleBranch();
	});
	$("#college").change(function(){
		toggleCollege();	
	});

});

