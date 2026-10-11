from memory.memory import Memory

memory = Memory()

memory.remember("name", "Jaguer", "profile", 10)
memory.remember("favorite_color", "Black", "preference", 8)

print("Search Results:")
print(memory.search("Black"))

print("\nAll Memories:")
print(memory.all())

memory.forget("favorite_color")

print("\nAfter Forget:")
print(memory.all())

# Add this at the very end
print("\nMemory Stats:")
print(memory.stats())