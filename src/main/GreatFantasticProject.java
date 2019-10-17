import static spark.Spark.port;
import org.apache.log4j.Logger;
import java.util.HashMap;
import java.util.Map;
import spark.ModelAndView;
import spark.template.mustache.MustacheTemplateEngine;
import static spark.Spark.get;
import static spark.Spark.post;

//Attempt to create an web app with Heroku ports

public class GreatFantasticProject {

    public static final String CLASSNAME="GauchoCourses";
    
    public static final Logger log = Logger.getLogger(GreatFantasticProject);

    public static void main(String[] args) {

    port(getHerokuAssignedPort());
    //easy read in terminal to find port number
    System.out.println("");
    System.out.println("");
    System.out.println("");
    System.out.println("");
    System.out.println("visit in browser: http://localhost:" + getHerokuAssignedPort());
    System.out.println("");
    System.out.println("");
    System.out.println("");
    System.out.println("");
    
        
    // hello.mustache file is in resources/templates directory
    get("/", (rq, rs) -> new ModelAndView(map, "mainpage.mustache"), new MustacheTemplateEngine());

    }
    
    static int getHerokuAssignedPort() {
        ProcessBuilder processBuilder = new ProcessBuilder();
        if (processBuilder.environment().get("PORT") != null) {
            return Integer.parseInt(processBuilder.environment().get("PORT"));
        }
        return 4567; //return default port if heroku-port isn't set (i.e. on localhost)
    }

    
}