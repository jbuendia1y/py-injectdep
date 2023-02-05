import injectdep
from injectdep import global_module
from dataclasses import dataclass

# --------------- Own Module ---------------
test_module = injectdep.Module()

print(test_module.dependencies)

@test_module.register
@dataclass
class Foo3:
    pass

print(test_module)

# ---------------  Global  ---------------

@global_module.register
class Foo:
    @classmethod
    def sum(self,a: int, b: int):
        return a + b

@global_module.register
class Bar:
    pass

@global_module.register
class Foo2:
    pass

@global_module.inject
def foo(c : Foo, b : Foo2):
    print(c.sum(10,20))

foo()

print(injectdep.global_module)
print(test_module)