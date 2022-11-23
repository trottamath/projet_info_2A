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

