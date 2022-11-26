This application is a cadastral API, its purpose is to answer to a choice among three possible requests from a user.

The user knows the INSEE codes of the french municipalities or parcels 
of which he is looking for the neighboring municipalities or parcels.

The user can run their requests either in the terminal (using View) or using FastAPI in a web browser.

Firstly, the user chooses from the following list of three requests:
1 - Municipalities contiguous to a given municipality
2- Parcels on the edge of its given municipality
3- Parcels bordering on a given parcel

Then, the user chooses from the proposed list of dates, which corresponds to the file date on the cadastral website. 
The user can choose “latest” to have the most recent information available, this choice also guarantees more speed by using a database.

Finally, the user manually enters the code of the reference municipality or parcel.
The request response time can be faster, especially for the first two requests, if the information is already present in the database, 
because it does not need to download and browse the cadastral files .

The proposed database is scalable. It is enriched with each new request, with automated management of the available memory space. 
Initially, the database is loaded for the “latest” date available on the cadastral site. 
This version limits the database to department 35, but it remains possible to launch a request for another department.

For example, if the user chooses the request 1 "bordering municipalities of a given municipality" for the 7th district of Marseille 
(INSEE code 13207) on the “latest” date, the application will return the list ['13201', '13206','13208'] corresponding to the 1st, 
6th and 8th districts of Marseille.

WARNING  for the first use: Create your database (cf. init_db.sql). To load a complete district in the database, for exemple for the district 13, use 
 InitialisationBdD(id_dep="13").chargement_bdd()