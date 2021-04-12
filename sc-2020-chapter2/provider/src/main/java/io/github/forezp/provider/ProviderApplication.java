package io.github.forezp.provider;

import org.springframework.beans.factory.annotation.Value;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.cloud.client.discovery.EnableDiscoveryClient;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

@SpringBootApplication
@RestController
@EnableDiscoveryClient
public class ProviderApplication {

    public static void main(String[] args) {
        SpringApplication.run(ProviderApplication.class, args);
    }


    @Value("${server.port}")
    String port;

    @GetMapping("/hi")
    public String hi(@RequestParam(value = "name", defaultValue = "forezp",required = false) String name) {
        return "hello " + name + ", i'm provider ,my port:" + port;

    }
}
