import java.utils.ArrayList;
import java.utils.List;
import..............

class Data(){
	String name;
	String color;
	float price;
	String description;
	Data(String name, String color, float price, String description){
		//constructor
		this.name = name;
		this.color = color;
		this.price = price;
		this.description = description;
	}

	public String getName(){
		return this.name();
	}
	//bunch of getters later...

	public void setName(String name){
		this.name = name;
	}
  //bunch of setter later...
  
	public String printInfo(){
		//ret
    as a String
	}
}

void theSecretSauce(){
	//super basic rendition of how the data looked at
	//import data into database
	List<Data> database = new ArrayList<>();
	List<String> keywords = new ArrayList<>();
	List<Data> output = new ArrayList<>();
	
	database.add(new Data(...));
	database.add(new Data(...));
	database.add(new Data(...));

	keywords.add("key");
	//one keyword for now
	//how to scale for multiple?
	//do we want the item with all the keywords together or do we want every thing that is related?
	//output based on the amount of keywords matched in one descriptions? Most at top?
	/*
	Ex: 
	input: keywords are basketball and shoes
	database includes: Spalding Basketball, Nike Lebron Basketball Shoes, Nike Free Run Running Shoes, Wilson Football
	output: Nike Lebron Basketball Shoes (2), Spalding Basketball (1), Nike Free Run (1) ????
	*/
  
  //for one keyword only at the moment
  //use another for loop? but that O(n^2) with a lot of keywords is a no go
	for(Data i : database){ 
		if(i.getDescription().contains(keywords.get(0)))	
			output.add(i);
	}
  
	for(Data d: output){
		d.printInfo();
	}
  
}
