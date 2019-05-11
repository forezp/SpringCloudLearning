package com.forezp.web;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.cloud.client.ServiceInstance;
import org.springframework.cloud.client.discovery.DiscoveryClient;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;

/**
 * Created by forezp on 2019/5/11.
 */

@RestController
public class ProviderController {

    Logger logger= LoggerFactory.getLogger(ProviderController.class);

    @Autowired
    DiscoveryClient discoveryClient;

    @GetMapping("/services")
    public String getServices(){
        List<String> serviceNames=discoveryClient.getServices();

        StringBuilder stringBuilder=new StringBuilder();
        for (String s: serviceNames){
            stringBuilder.append(s).append("\n");
            List<ServiceInstance> serviceInstances=discoveryClient.getInstances(s);
            if(serviceInstances!=null&&serviceInstances.size()>0){
                for (ServiceInstance serviceInstance: serviceInstances){
                    logger.info("serviceName:"+s+" host:"+serviceInstance.getHost()+" port:"+serviceInstance.getPort());
                }
            }
        }
        return stringBuilder.toString();
    }

    @GetMapping("/hi")
    public String hi(@RequestParam(value = "name",defaultValue = "forezp",required = false)String name){

        return "hi "+name;
    }
}
