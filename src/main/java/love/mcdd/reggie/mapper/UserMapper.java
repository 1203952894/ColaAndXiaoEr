package love.mcdd.reggie.mapper;

import com.baomidou.mybatisplus.core.mapper.BaseMapper;
import love.mcdd.reggie.entity.User;
import org.apache.ibatis.annotations.Mapper;

@Mapper
public interface UserMapper extends BaseMapper<User> {
}