package love.mcdd.reggie.dto;


import lombok.Data;
import love.mcdd.reggie.entity.Dish;
import love.mcdd.reggie.entity.DishFlavor;

import java.util.ArrayList;
import java.util.List;

@Data
public class DishDto extends Dish {

    private List<DishFlavor> flavors = new ArrayList<>();

    private String categoryName;

    private Integer copies;
}
