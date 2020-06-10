package com.forezp.client;

import org.springframework.cloud.openfeign.FeignClient;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;

/**
 * Created by forezp on 2019/5/11.
 */
@FeignClient("nacos-provider")
public interface ProviderClient {

    @GetMapping("/hi")
    String hi(@RequestParam(value = "name", defaultValue = "forezp", required = false) String name);
}


