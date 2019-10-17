import static spark.Spark.port;
import org.apache.log4j.Logger;
import spark.ModelAndView;
import spark.template.mustache.MustacheTemplateEngine;
import static spark.Spark.get;
import static spark.Spark.post;

//Attempt to create an web app with Heroku ports

public class GreatFantasticProject {

    public static final String CLASSNAME="GauchoCourses";
    
    public static final Logger log = Logger.getLogger(GreatFantasticProject);
    //Logger used to log bugs and such in terminal 
    
    public static void main(String[] args) {

        port(getHerokuAssignedPort());
        
        //bunch of spaces so that it is easy to read in terminal to find port number
        System.out.println("");
        System.out.println("");
        System.out.println("");
        System.out.println("");
        System.out.println("visit in browser: http://localhost:" + getHerokuAssignedPort());
        LOGGER.log("PORT:" + getHerokuAssignedPort());
        System.out.println("");
        System.out.println("");
        System.out.println("");
        System.out.println("");
        
        //currently just main page and random page
        //we will see if additional pages will be necessary in the future
        // hello.mustache file is in resources/templates directory
        get("/", (rq, rs) -> new ModelAndView(map, "mainpage.mustache"), new MustacheTemplateEngine());
        
        get("/page2", (rq, rs) -> new ModelAndView(map, "page2.mustache"), new MustacheTemplateEngine());

    }
    
    static int getHerokuAssignedPort() {
        ProcessBuilder processBuilder = new ProcessBuilder();
        if (processBuilder.environment().get("PORT") != null) {
            return Integer.parseInt(processBuilder.environment().get("PORT"));
        }
        //return default port if heroku-port isn't set (i.e. on localhost)
        return 4567; 
    }
}
