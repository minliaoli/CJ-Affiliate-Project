public class DataModelResource {
    private String name;
    private String color;
    private float price;
    private String description;
    public DataModelResource(String name, String color, float price, String description){
        //constructor
        this.name = name;
        this.color = color;
        this.price = price;
        this.description = description;
    }

    public String getName(){
        return this.name;
    }
    public String getColor() {
        return this.color;
    }
    public float getPrice() {
        return this.price;
    }
    public String getDescription() {
        return this.description;
    }
    public void setName(String name){
        this.name = name;
    }
    public void setColor(String color){
        this.color = color;
    }
    public void setPrice(float price){
        this.price = price;
    }
    public void setDescription(String description){
        this.description = description;
    }
    public String printInfo(){
        //returns all info of the data
        return "data: " + this.getName() + "\n" + this.getColor() + "\n" + this.getPrice() + "\n" + this.getDescription() + "\n";
    }

}
