import javafx.scene.chart.PieChart;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.lang.reflect.GenericDeclaration;
import java.util.ArrayList;
import java.util.List;

@RestController
public class Server {
        private List<DataModelResource> dataModelResource = new ArrayList();

        public Server(List<DataModelResource> data){
            for(DataModelResource i: data)
                dataModelResource.add(i);
        }

        @GetMapping(value = "/")
        public ResponseEntity get() {
            return ResponseEntity.ok(dataModelResource);
        }

        @GetMapping(value = "/data")
        public ResponseEntity getData(@RequestParam(value="keyword") String keyword) {
            DataModelResource itemToReturn = null;
            for(DataModelResource data : myBucketList){
                if(bucket.getDescription() == id)
                    itemToReturn = bucket;
            }

            return ResponseEntity.ok(itemToReturn);
        }

        @PostMapping(value = "/")
        public ResponseEntity addToData(@RequestParam(value="data") DataModelResource data) {
            DataModelResource.add(data);
            return ResponseEntity.ok(dataModelResource);
        }
    }
}
