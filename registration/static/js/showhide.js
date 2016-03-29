function toggleBranch(){
	if ($("#course").val()=="Btech" || $("#course").val()=="Mtech")
		$("#branch").show();
	else
		$("#branch").hide();
}

$(document).ready(function(){
	$("#course").change(function(){
		toggleBranch();	
	});

});

window.onload = function() {

  if(localStorage){
    console.log(localStorage)
    var name= localStorage.getItem('name')
    var email= localStorage.getItem('email')
    var course= localStorage.getItem('course')
    var branch= localStorage.getItem('branch')
    var contact= localStorage.getItem('contact')
    var college= localStorage.getItem('college')
    var year= localStorage.getItem('year')

    document.getElementById('name').value=name;
    document.getElementById('email').value=email
    document.getElementById('course').value=course
    document.getElementById('branch').value=branch
    document.getElementById('contact').value=contact
    document.getElementById('college').value=college
    document.getElementById('year').value=year

    document.getElementById('registerform').addEventListener('submit',function(){
      var name = document.getElementById('name').value;
      var email = document.getElementById('email').value;
      var course = document.getElementById('course').value;
      var branch = document.getElementById('branch').value;
      var contact = document.getElementById('contact').value;
      var college = document.getElementById('college').value;
      var year = document.getElementById('year').value;

      localStorage.setItem('name',name);
      localStorage.setItem('email',email);
      localStorage.setItem('course',course);
      localStorage.setItem('branch',branch);
      localStorage.setItem('contact',contact);
      localStorage.setItem('college',college);
      localStorage.setItem('year',year);


    });
  }
}

$(function(){
	  var collegelist = [];
        
           collegelist.push("ABES Engineering College, Ghaziabad");
        
           collegelist.push("ACE Engineering College, Ghatsekar");
        
           collegelist.push("Acharya Narendra Dev College [ANDC], New Delhi");
        
           collegelist.push("AES Institute of Computer Studies, Ahmedabad");
        
           collegelist.push("Agartala Government Medical College [AGMC], Agartala");
        
           collegelist.push("Ahmedabad University, Ahmedabad");
        
           collegelist.push("AISSMS Insititute of Information Technology, Pune");
        
           collegelist.push("Ajay Kumar Garg Engineering College [AKGEC], Ghaziabad");
        
           collegelist.push("Ambedkar Institute of Advanced Communication Technologies & Research [AIACTR], New Delhi");
        
           collegelist.push("Amity Institute of Education, New Delhi");
        
           collegelist.push("Amity Law School, Noida (IP University)");
        
           collegelist.push("Amity School of Engineering & Technology [ASET], IP University, New Delhi");
        
           collegelist.push("Amity University, Gwalior");
        
           collegelist.push("Amity University, Noida");
        
           collegelist.push("Amrapali Institute Of Technology and Sciences [AITS], Haldwani");
        
           collegelist.push("Anand Institute of Higher Technology [AIHT], Chennai");
        
           collegelist.push("Annamacharya Institute of Technology & Sciences [AITS], Kadapa");
        
           collegelist.push("ARAI Academy, Pune");
        
           collegelist.push("Army Institute of Technology & Management [AITM], Greater Noida");
        
           collegelist.push("ARYA Institute of Engineering & Technology [AIET[, Jaipur");
        
           collegelist.push("Aryabhatta College, New Delhi");
        
           collegelist.push("AS College, Deoghar");
        
           collegelist.push("Ashoka University, Sonipat");
        
           collegelist.push("Assam Engineering College, Guwahati");
        
           collegelist.push("Atharva College of Engineering [ACE], Mumbai");
        
           collegelist.push("Atma Ram Sanatan Dharam College [ARSD], New Delhi");
        
           collegelist.push("Banaras Hindu University [BHU], Varanasi");
        
           collegelist.push("Banarsidas Chandiwala Institute of Physiotherapy [BCIP], New Delhi");
        
           collegelist.push("Banasthali Vidyapith (Banasthali University)");
        
           collegelist.push("Bangalore Institute of Technology [BIT], Bengaluru");
        
           collegelist.push("Barasat Government College [BGC], Kolkata");
        
           collegelist.push("Bhagwan Parshuram Institute of Technology [BPIT], New Delhi");
        
           collegelist.push("Bhagwant University, Ajmer");
        
           collegelist.push("Bharathiar University, Coimbatore");
        
           collegelist.push("Bharati College, New Delhi");
        
           collegelist.push("Bharati Vidyapeeth Institute of Computer Applications & Management, New Delhi");
        
           collegelist.push("Bharati Vidyapeeth University Institute of Management & Research [BVIMR], New Delhi");
        
           collegelist.push("Bharati Vidyapeeth's College of Engineering [BVP], New Delhi");
        
           collegelist.push("Bheema Institute of Technology and Science [BITS], Adoni");
        
           collegelist.push("Bhilai Institute of Technology [BIT], Durg");
        
           collegelist.push("Bhim Rao Ambedkar College [BRAC], New Delhi");
        
           collegelist.push("Bidar Institute of Medical Sciences, Bidar");
        
           collegelist.push("Birla Institute of Technology and Science [BITS], Goa Campus ");
        
           collegelist.push("Birla Institute of Technology and Science [BITS], Pilani");
        
           collegelist.push("Birla Institute of Technology [BIT], Jaipur");
        
           collegelist.push("Birla Vishvakarma Mahavidyalay Engineering College [BVMEC], Anand");
        
           collegelist.push("BMS College of Engineering, Bengaluru");
        
           collegelist.push("BMS Institute of Technology, Bengaluru");
        
           collegelist.push("BP Poddar Institute of Management and Technology [BPPIMT], Kolkata");
        
           collegelist.push("Brainware Group of Institutions, Kolkata");
        
           collegelist.push("BS Abdur Rahman University [BSARU], Chennai");
        
           collegelist.push("BVB College of Engineering and Technology [BVBCET], Hubli");
        
           collegelist.push("Canara Engineering College, Mangalore");
        
           collegelist.push("Career College, Bhopal");
        
           collegelist.push("Centre for Development of Advanced Computing [CDAC], Noida");
        
           collegelist.push("Charotar University of Science and Technology, Anand");
        
           collegelist.push("Chitkara University, Chandigarh");
        
           collegelist.push("Christ University, Bangalore");
        
           collegelist.push("Cluster Innovation Centre [CIC], University of Delhi");
        
           collegelist.push("Cochin University Of Science and Technology [CUSAT], Kochi");
        
           collegelist.push("Coimbatore Institute of Engineering and Technology [CIET], Coimbatore");
        
           collegelist.push("College of Engineering [CETKR], Trikaripur");
        
           collegelist.push("College of Nursing, Dr. Ram Manohar Lohia Hospital, New Delhi");
        
           collegelist.push("College of Vocational Studies [CVS], New Delhi");
        
           collegelist.push("Corporate Institute of Research and Technology [CIRT], Bhopal ");
        
           collegelist.push("Cummins College Of Engineering for Women [CCOEW], Pune");
        
           collegelist.push("CV Raman College Of Engineering [CVRCE], Bhubaneshwar");
        
           collegelist.push("Dayananda Sagar Institutions (Kumaraswamy Campus), Bangalore");
        
           collegelist.push("Deccan College of Medical Sciences [DCMS], Hyderabad");
        
           collegelist.push("Deenbandhu Chhotu Ram University Of Science & Technology, Sonepat");
        
           collegelist.push("Delhi College of Arts and Commerce [DCAC], New Delhi");
        
           collegelist.push("Delhi School of Business [DSB], New Delhi");
        
           collegelist.push("Delhi Technological University [DTU], New Delhi");
        
           collegelist.push("Department of Management Science, Pune University, Pune");
        
           collegelist.push("Deshbandhu College, New Delhi");
        
           collegelist.push("Dhanalakshmi Srinivasan College of Engineering & Technology [DSCET], Chennai");
        
           collegelist.push("DIT University, Dehradun");
        
           collegelist.push("Doaba Polytechnic College, SBS Nagar (Punjab)");
        
           collegelist.push("Don Bosco Institute Of Technology [DBIT], Mumbai");
        
           collegelist.push("Dr. Sudhir Chandra Sur Degree Engineering College, Kolkata");
        
           collegelist.push("DS College, Katihar");
        
           collegelist.push("Dyal Singh College, New Delhi");
        
           collegelist.push("Easwari Engineering College, Chennai");
        
           collegelist.push("Fairfield Institute of Management & Technology [FIMT], New Delhi");
        
           collegelist.push("Fergusson College, Pune");
        
           collegelist.push("Finolex Academy of Management and Technology [FAMT], Ratnagiri");
        
           collegelist.push("Footwear Design & Development Institute [FDDI], Noida");
        
           collegelist.push("FORE School of Management, New Delhi");
        
           collegelist.push("Gauhati University, Guwahati");
        
           collegelist.push("GB Pant Government Engineering College, New Delhi");
        
           collegelist.push("Geethanjali College of Engineering and Technology [GCET], Hyderabad");
        
           collegelist.push("Gitarattan International Business School, New Delhi");
        
           collegelist.push("Globsyn Business School, Kolkata");
        
           collegelist.push("GLS Institute of Commerce, Ahmedabad");
        
           collegelist.push("Goa Medical College");
        
           collegelist.push("Gokaraju Rangaraju Institute of Engineering & Technology [GRIET], Hyderabad");
        
           collegelist.push("Government College of Engineering , Salem");
        
           collegelist.push("Government Engineering College [GEC], Bharatpur");
        
           collegelist.push("Government Engineering College, Bikaner ");
        
           collegelist.push("Government Medical College, Raigarh");
        
           collegelist.push("Govt Polytechnic College, Hamirpur");
        
           collegelist.push("Gudlavalleru Engineering College");
        
           collegelist.push("Guru Ghasidas University [GGU], Bilaspur");
        
           collegelist.push("Guru Nanak Dev Polytechnic College, New Delhi");
        
           collegelist.push("Guru Nanak Dev University, Amritsar");
        
           collegelist.push("Guru Nanak Institute of Technology [GNIT], Kolkata");
        
           collegelist.push("Guru Teg Bahadur Institute of Technology [GTBIT], New Delhi");
        
           collegelist.push("Haldia Institute of Technology, Haldia");
        
           collegelist.push("Hansraj College, New Delhi");
        
           collegelist.push("Harcourt Butler Technological Institute [HBTI], Kanpur");
        
           collegelist.push("Havanur College of Law, Bangalore");
        
           collegelist.push("Hindu College, Delhi University");
        
           collegelist.push("HMR Institute of Technology & Management, New Delhi");
        
           collegelist.push("HPT Arts & RYK Science College, Nashik");
        
           collegelist.push("HR College of Commerce and Economics, Mumbai");
        
           collegelist.push("ICFAI Business School [IBS], Hyderabad");
        
           collegelist.push("ICLES Motilal Jhunjhunwala College, Navi Mumbai");
        
           collegelist.push("Ideal Institute of Technology, Ghaziabad");
        
           collegelist.push("IILM College of Engineering and Technology, Greater Noida");
        
           collegelist.push("IIMT College of Engineering, Greater Noida");
        
           collegelist.push("IMS Engineering College, Ghaziabad");
        
           collegelist.push("Indian Aerospace & Engineering, Navi Mumbai");
        
           collegelist.push("Indian Institute of Engineering Science and Technology [IIEST], Shibpur");
        
           collegelist.push("Indian Institute of Foreign Trade [IIFT], Kolkata");
        
           collegelist.push("Indian Institute of Foreign Trade [IIFT], New Delhi");
        
           collegelist.push("Indian Institute of Information Technology [IIIT], Allahabad");
        
           collegelist.push("Indian Institute of Management [IIM], Ahmedabad");
        
           collegelist.push("Indian Institute of Management [IIM], Bangalore");
        
           collegelist.push("Indian Institute of Management [IIM], Calcutta");
        
           collegelist.push("Indian Institute of Management [IIM], Indore");
        
           collegelist.push("Indian Institute of Management [IIM], Rohtak");
        
           collegelist.push("Indian Institute of Management [IIM], Shillong");
        
           collegelist.push("Indian Institute of Technology [IIT], Bombay");
        
           collegelist.push("Indian Institute of Technology [IIT], Delhi");
        
           collegelist.push("Indian School of Business [ISB], Hyderabad");
        
           collegelist.push("Indian School of Mines [ISM], Dhanbad");
        
           collegelist.push("Indira Gandhi Delhi Technical University For Women [IGDTUW], New Delhi");
        
           collegelist.push("Indraprastha Engineering College [IPEC], Ghaziabad");
        
           collegelist.push("Indraprastha Institute of Information Technology [IIIT], New Delhi");
        
           collegelist.push("Indus University, Ahmedabad");
        
           collegelist.push("Institute of Chemical Technology [ICT], Mumbai");
        
           collegelist.push("Institute of Engineering & Management [IEM], Kolkata");
        
           collegelist.push("Institute of Engineering and Technology, Devi Ahilya Vishwavidyalaya [IET-DAVV], Indore");
        
           collegelist.push("Institute of Information Technology & Management [IITM], New Delhi");
        
           collegelist.push("Institute of Management Studies [IMS], Ghaziabad");
        
           collegelist.push("Institute of Management Studies [IMS], Noida");
        
           collegelist.push("Institute of Management Studies [IMS], Ropar");
        
           collegelist.push("Institute of Management Studies, Devi Ahilya University, Indore");
        
           collegelist.push("Institute of Management Technology [IMT], Ghaziabad");
        
           collegelist.push("Institute of Marketing and Management [IMM], New Delhi");
        
           collegelist.push("Institute of Technical Education and Research [ITER], Bhubaneshwar");
        
           collegelist.push("International Institute of Information Technology [IIIT], Bangalore");
        
           collegelist.push("International Institute of Information Technology [IIIT], Hyderabad");
        
           collegelist.push("IQ City Medical College, Durgapur");
        
           collegelist.push("Jadavpur University, Kolkata");
        
           collegelist.push("Jagannath International Management School [JIMS], New Delhi (Kalkaji)");
        
           collegelist.push("Jai Bharath College, Arackappady, Cochin");
        
           collegelist.push("Jai Hind College, Mumbai");
        
           collegelist.push("Jaipur Engineering College and Research Centre [JECRC], Jaipur");
        
           collegelist.push("Jaipuria Institute of Management [JIM], Lucknow");
        
           collegelist.push("Jaipuria Institute of Management, Ghaziabad");
        
           collegelist.push("Jamia Hamdard, New Delhi");
        
           collegelist.push("Jamia Millia Islamia, New Delhi");
        
           collegelist.push("Jawaharlal Nehru Engineering College [JNEC], Aurangabad");
        
           collegelist.push("Jawaharlal Nehru National College of Engineering [JNNCE], Shivamogga");
        
           collegelist.push("Jawaharlal Nehru Technological University [JNTU], Hyderabad");
        
           collegelist.push("Jawaharlal Nehru University [JNU], New Delhi");
        
           collegelist.push("Jaypee Institute of Information Technology [JIIT], Noida (Sector 128)");
        
           collegelist.push("Jaypee Institute of Information Technology [JIIT], Noida (Sector 62)");
        
           collegelist.push("Jesus and Mary College [JMC], New Delhi");
        
           collegelist.push("JIET Group of Institutions, Jodhpur");
        
           collegelist.push("JNTU College of Engineering, Pulivendula");
        
           collegelist.push("JSS Academy of Technical Education [JSSATE], Noida");
        
           collegelist.push("Kakatiya Institute of Technology and Science [KITS], Warangal");
        
           collegelist.push("Kamala Nehru College [KNC], Delhi University");
        
           collegelist.push("Karnataka State Open University [KSOU]");
        
           collegelist.push("KES Shroff College, Mumbai");
        
           collegelist.push("Keshav Mahavidyalaya, New Delhi");
        
           collegelist.push("KIIT University, Bhubaneshwar");
        
           collegelist.push("Kirori Mal College [KMC], New Delhi");
        
           collegelist.push("KK Wagh Institute of Engineering Education and Research, Nashik");
        
           collegelist.push("KMP College of Engineering [KMPCE], Ernakulam");
        
           collegelist.push("Kongu Engineering College, Perundurai");
        
           collegelist.push("KPB Hinduja College of Commerce, Mumbai");
        
           collegelist.push("Kristu Jayanti College, Bengaluru");
        
           collegelist.push("L J Institute Of Computer Applications, Ahmedabad");
        
           collegelist.push("Lachoo Memorial College of Science and Technology [LMCST], Jodhpur");
        
           collegelist.push("Lady Hardinge Medical College [LHMC], New Delhi");
        
           collegelist.push("Lady Shri Ram College for Women [LSR], New Delhi");
        
           collegelist.push("Lal Bahadur Shastri Institute of Management [LBSIM], New Delhi");
        
           collegelist.push("Lalbhai Dalpatbhai College of Engineering [LDCE], Ahmedabad");
        
           collegelist.push("LDPR Institute of Technology and Research, Gandhinagar");
        
           collegelist.push("Lords Institute of Engineering & Technology [LIET], Hyderabad");
        
           collegelist.push("Lords Universal College, Mumbai");
        
           collegelist.push("Lovely Professional University [LPU], Phagwara");
        
           collegelist.push("LS Raheja College of Arts & Commerce, Mumbai");
        
           collegelist.push("Madhav Institute of Technology and Science [MITS], Gwalior");
        
           collegelist.push("Madras Institute Of Technology [MIT], Chennai");
        
           collegelist.push("Maharaja Agrasen Institute of Technology [MAIT], New Delhi");
        
           collegelist.push("Maharaja Surajmal Institute Of Technology [MSIT], New Delhi");
        
           collegelist.push("Maharana Pratap College of Technology [MPCT], Gwalior");
        
           collegelist.push("Maharashtra Institute Of Technology [MIT], Pune");
        
           collegelist.push("Maharishi Arvind International Institute of Technology, Kota");
        
           collegelist.push("Mahatma Gandhi Institute of Technology [MGIT], Hyderabad");
        
           collegelist.push("Mahatma Gandhi Mission's College of Engineering & Technology [MGMCET], Noida");
        
           collegelist.push("Maitreyi College, New Delhi");
        
           collegelist.push("Malini Kishore Sanghvi College of Commerce and Economics, Mumbai");
        
           collegelist.push("Malla Reddy College of Pharmacy [MRCP], Hyderabad");
        
           collegelist.push("MAM College Of Engineering And Technology [MAMCET], Trichy");
        
           collegelist.push("Management Development Institute [MDI], Gurgaon");
        
           collegelist.push("Mangalayatan University, Aligarh");
        
           collegelist.push("Manipal Institute of Technology [MIT], Manipal");
        
           collegelist.push("Manipal University, Jaipur");
        
           collegelist.push("Marwadi Education Foundation's Group of Institutions [MEFGI], Rajkot");
        
           collegelist.push("Matrusri Institute of Post Graduate Studies [MIPGS], Hyderabad");
        
           collegelist.push("MATS University, Raipur");
        
           collegelist.push("Maulana Azad National Institute of Technology [MANIT], Bhopal");
        
           collegelist.push("Meerut Institute of Engineering and Technology [MIET], Meerut");
        
           collegelist.push("Miranda House, New Delhi");
        
           collegelist.push("MIT College of Engineering [MITCOE], Pune");
        
           collegelist.push("MIT School Of Management, Pune");
        
           collegelist.push("Mithibai College, Mumbai");
        
           collegelist.push("ML Dahanukar College of Commerce, Mumbai");
        
           collegelist.push("MMK College of Commerce and Economics, Mumbai");
        
           collegelist.push("Model Institute of Engineering & Technology, Jammu");
        
           collegelist.push("Moradabad Institute of Technology [MIT], Moradabad");
        
           collegelist.push("Motilal Nehru College (Evening) [MLNC], New Delhi");
        
           collegelist.push("Motilal Nehru College [MLNC], New Delhi");
        
           collegelist.push("Motilal Nehru National Institute of Technology [MNNIT], Allahabad");
        
           collegelist.push("Mount Carmel College, Bengaluru");
        
           collegelist.push("MPM Government First Grade College, Karkala");
        
           collegelist.push("MS Ramaiah Institute of Technology [MSRIT], Bengaluru");
        
           collegelist.push("Mukesh Patel School of Technology Management & Engineering (MPSTME) - NMIMS, Mumbai");
        
           collegelist.push("Mukesh Patel School Of Technology Management & Engineering, Shirpur Campus");
        
           collegelist.push("MVJ College of Education [MVJCOE], Bengaluru");
        
           collegelist.push("MVJ College of Engineering [MVJCE], Bangalore");
        
           collegelist.push("Nagindas Khandwala College, Mumbai");
        
           collegelist.push("Nalanda College of Law, Mumbai");
        
           collegelist.push("Narayana Medical College, Nellore");
        
           collegelist.push("Narsee Monjee College of Commerce and Economics, Mumbai");
        
           collegelist.push("Narsee Monjee Institute of Management Studies [NMIMS], Hyderabad");
        
           collegelist.push("Narsee Monjee Institute of Management Studies [NMIMS], Mumbai");
        
           collegelist.push("National Institute of Fashion Technology [NIFT], Chennai");
        
           collegelist.push("National Institute of Fashion Technology [NIFT], Patna");
        
           collegelist.push("National Institute of Technology [NIT], Agartala");
        
           collegelist.push("National Institute of Technology [NIT], Calicut");
        
           collegelist.push("National Institute of Technology [NIT], Durgapur");
        
           collegelist.push("National Institute of Technology [NIT], Hamirpur");
        
           collegelist.push("National Institute of Technology [NIT], Jalandhar");
        
           collegelist.push("National Institute of Technology [NIT], Kurukshetra");
        
           collegelist.push("National Institute of Technology [NIT], Raipur");
        
           collegelist.push("National Institute of Technology [NIT], Rourkela");
        
           collegelist.push("National Institute of Technology [NIT], Srinagar");
        
           collegelist.push("National Institute of Technology [NIT], Surathkal");
        
           collegelist.push("National Institute of Technology [NIT], Warangal");
        
           collegelist.push("National Power Training Institute [NPTI], Durgapur");
        
           collegelist.push("National Power Training Institute [NPTI], New Delhi");
        
           collegelist.push("NCRD's Sterling Institute of Management Studies, Navi Mumbai ");
        
           collegelist.push("NDMVP College of Engineering, Nashik");
        
           collegelist.push("Netaji Subhas Institute of Technology [NSIT], New Delhi");
        
           collegelist.push("New Delhi Institute of Management [NDIM], New Delhi");
        
           collegelist.push("New Horizon College of Engineering, Bengaluru");
        
           collegelist.push("Nirma University, Ahmedabad");
        
           collegelist.push("Nitte Meenakshi Institute of Technology [NMIT], Bangalore");
        
           collegelist.push("NM Institute of Engineering and Technology [NMIET], Bhubaneshwar");
        
           collegelist.push("Noble Group of Institutions, Junagadh");
        
           collegelist.push("Northern India Engineering College [NIEC], New Delhi");
        
           collegelist.push("Nowrosjee Wadia College, Pune");
        
           collegelist.push("NSHM Knowledge Campus, Kolkata");
        
           collegelist.push("Oriental College of Technology [OCT], Bhopal");
        
           collegelist.push("Oriental University, Indore");
        
           collegelist.push("Padre Conceicao College of Engineering [PCCE], Goa");
        
           collegelist.push("Pandit Deendayal Petroleum University [PDPU], Gandhinagar");
        
           collegelist.push("Panimalar Engineering College, Chennai");
        
           collegelist.push("Panjab University, Chandigarh");
        
           collegelist.push("Parul University");
        
           collegelist.push("Patna University");
        
           collegelist.push("PDM College of Engineering, Bahadurgarh");
        
           collegelist.push("PERI Institute Of Technology, Chennai");
        
           collegelist.push("PES University [PESIT], Bangalore");
        
           collegelist.push("PGDAV College, New Delhi");
        
           collegelist.push("Pillai Institute of Management Studies and Research [PIMSR], Navi Mumbai");
        
           collegelist.push("Pondicherry University");
        
           collegelist.push("Pravin Patil College Of Diploma Engineering and Technology, Mira Bhayandar");
        
           collegelist.push("PSG College Of Technology, Coimbatore");
        
           collegelist.push("PSGR Krishnammal College for Women, Coimbatore");
        
           collegelist.push("PSNA College of Engineering and Technology, Dindigul");
        
           collegelist.push("Pune Vidhyarthi Griha's College of Engineering and Technology [PVGCOET], Pune");
        
           collegelist.push("Rajdhani College, Delhi University");
        
           collegelist.push("Rajiv Gandhi Institute of Technology [RGIT], Mumbai");
        
           collegelist.push("Ramdeobaba College of Engineering and Management [RCOEM], Nagpur");
        
           collegelist.push("Ramjas College, New Delhi");
        
           collegelist.push("Rao Bahadur Y Mahabaleswarappa Engineering College [RYMEC], Bellary");
        
           collegelist.push("Rayat Bahra Group of Institutes, Hoshiarpur");
        
           collegelist.push("Rizvi College of Arts, Science & Commerce, Mumbai");
        
           collegelist.push("RMK Engineering College, Thiruvallur");
        
           collegelist.push("RN College of Engineering and Technology [RNCET], Panipat");
        
           collegelist.push("RV College Of Engineering [RVCE], Bengaluru");
        
           collegelist.push("Samrat Ashok Technological Institute [SAIT], Vidisha");
        
           collegelist.push("Sardar Vallabhbhai National Institute of Technology [SVNIT], Surat");
        
           collegelist.push("Sardar Vallabhbhai Patel Institute of Technology, Vasad");
        
           collegelist.push("SASTRA University, Thanjavur");
        
           collegelist.push("Sathaye College, Mumbai");
        
           collegelist.push("Satyawati College (Evening), New Delhi");
        
           collegelist.push("Saveetha Engineering College, Chennai");
        
           collegelist.push("School of Inspired Leadership [SOIL], Gurgaon");
        
           collegelist.push("School of Open Learning [SOL], New Delhi");
        
           collegelist.push("SDM Institute for Management Development, Mysore");
        
           collegelist.push("Seacom Engineering College, Howrah");
        
           collegelist.push("Seth GS Medical College [KEM], Mumbai");
        
           collegelist.push("Seth Jai Parkash Mukand Lal Institute Of Engineering And Technology [JMIT], Radaur");
        
           collegelist.push("Shaheed Bhagat Singh College, New Delhi");
        
           collegelist.push("Shaheed Sukhdev College of Business Studies [SSCBS], New Delhi");
        
           collegelist.push("Shanmuganathan Engineering College, Pudukkottai");
        
           collegelist.push("Sharda University, Greater Noida");
        
           collegelist.push("Shri Guru Ram Rai PG College, Dehradun");
        
           collegelist.push("Shri Mata Vaishno Devi University [SMVDU], Jammu");
        
           collegelist.push("Shri Ram College of Commerce [SRCC], New Delhi");
        
           collegelist.push("Shri S'ad Vidya Mandal Institute Of Technology, Bharuch");
        
           collegelist.push("Shri Shankaracharya Technical Campus, Bhilai, Chhattisgarh");
        
           collegelist.push("Shyam Lal College, Delhi University");
        
           collegelist.push("Sibsagar College, Joysagar");
        
           collegelist.push("Sibsagar Commerce College, Sivasagar");
        
           collegelist.push("Siddaganga Institute of Technology [SIT], Tumkur");
        
           collegelist.push("Siddharth College of Arts, Science & Commerce, Mumbai");
        
           collegelist.push("SIES (Nerul) College of Arts, Science & Commerce, Mumbai");
        
           collegelist.push("Sigma Group of Institutes, Vadodara");
        
           collegelist.push("Sikkim Manipal University, Gangtok");
        
           collegelist.push("Sinhgad Academy of Engineering, Pune");
        
           collegelist.push("Sivanath Sastri College, Kolkata");
        
           collegelist.push("Smt. Chandibai Himathmal Mansukhani College, Ulhasnagar");
        
           collegelist.push("Sreenidhi Institute of Science and Technology [SNIST], Hyderabad");
        
           collegelist.push("Sri Aurobindo College, New Delhi");
        
           collegelist.push("Sri Bhagawan Mahaveer Jain College, Bengaluru");
        
           collegelist.push("Sri Guru Nanak Dev Khalsa College [SGNDKC], New Delhi");
        
           collegelist.push("Sri Guru Teg Bahadur Khalsa College [SGTB], New Delhi");
        
           collegelist.push("Sri Jayachamarajendra College of Engineering [SJCE], Mysore");
        
           collegelist.push("Sri Kengal Hanumanthaiah Law College, Kolar");
        
           collegelist.push("Sri Ramakrishna Engineering College [SREC], Coimbatore");
        
           collegelist.push("Sri Ramakrishna Institute of Technology [SRIT], Coimbatore");
        
           collegelist.push("Sri Sairam Engineering College, Chennai");
        
           collegelist.push("Sri Venkateswara College of Engineering [SVCE], Sriperumbudur ");
        
           collegelist.push("SRM University (Ramapuram Campus), Chennai");
        
           collegelist.push("SRM University, Chennai (Kattankulathur Campus)");
        
           collegelist.push("SSM College of Engineering and Technology, Baramulla");
        
           collegelist.push("St Joseph's Institute of Technology, Chennai");
        
           collegelist.push("St. Francis Institute of Technology [SFIT], Mumbai");
        
           collegelist.push("St. John College Of Engineering And Technology [SJCET], Palghar");
        
           collegelist.push("St. Joseph's College of Engineering, Chennai");
        
           collegelist.push("St. Thomas' College of Engineering & Technology [STCET], Kolkata");
        
           collegelist.push("St. Xavier's College, Kolkata");
        
           collegelist.push("St. Xavier's College, Palayamkottai");
        
           collegelist.push("Sydenham Institute of Management Studies, Research and Entrepreneurship Education, Mumbai");
        
           collegelist.push("Symbiosis Center for Distance Learning [SCDL]");
        
           collegelist.push("Symbiosis Centre for Management Studies [SCMS], Pune");
        
           collegelist.push("Symbiosis Institute of Business Management [SIBM], Pune");
        
           collegelist.push("Symbiosis Institute of International Business [SIIB], Pune");
        
           collegelist.push("TERI University, New Delhi");
        
           collegelist.push("Thapar University, Patiala");
        
           collegelist.push("Theem College of Engineering, Palghar");
        
           collegelist.push("TIT Group of Institutions, Bhopal");
        
           collegelist.push("Trident Group of Institutions, Bhubaneshwar");
        
           collegelist.push("Trinity Institute of Professional Studies [TIPS], New Delhi");
        
           collegelist.push("United College of Engineering & Research [UCER], Allahabad");
        
           collegelist.push("University Institute of Engineering and Technology [UIET], Kurukshetra");
        
           collegelist.push("University of  Petroleum & Energy Studies [UPES], Dehradun");
        
           collegelist.push("University of Lucknow");
        
           collegelist.push("University of Mysore");
        
           collegelist.push("University Of North Bengal, Darjeeling");
        
           collegelist.push("University School of Information & Communication Technology [USICT], IP University");
        
           collegelist.push("University Visvesvaraya College of Engineering [UVCE], Bengaluru");
        
           collegelist.push("Vasavi College of Engineering [VCE], Hyderabad");
        
           collegelist.push("VELS University, Chennai");
        
           collegelist.push("Versatile Business School, Chennai");
        
           collegelist.push("VG Vaze College, Mumbai");
        
           collegelist.push("Vidya College of Engineering [VCE], Meerut");
        
           collegelist.push("Vidyalankar Institute of Technology [VIT], Mumbai");
        
           collegelist.push("VIT University, Vellore");
        
           collegelist.push("Vivekananda Institute of Professional Studies [VIPS], New Delhi");
        
           collegelist.push("VPM RZ Shah College of Arts, Science & Commerce");
        
           collegelist.push("VSM Institute of Aerospace Engineering and Technology, Bengaluru");
        
           collegelist.push("Zakir Husain Delhi College, New Delhi");

  $("#college").autocomplete({
    source: collegelist ,
    minLength: 2,
  });
});