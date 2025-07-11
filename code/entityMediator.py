from code import entity
from code.enemy import Enemy


class entityMediator:

    @staticmethod
    def __verify_collision_window(ent: entity):
        if isinstance(ent, Enemy):
            if ent.rect.right < 0:
                ent.health = 0
        pass

    @staticmethod
    def verify_collision(entity_list: list[entity]):
        for i in range(len(entity_list)):
            test_entity = entity_list[i]
            entityMediator.__verify_collision_window(test_entity)

    @staticmethod
    def verify_health(entity_list: list[entity]):
        for ent in entity_list:
            if ent.health <= 0:
                entity_list.remove(ent)
