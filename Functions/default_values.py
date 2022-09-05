def describe_pet(pet_name, animal_typed='dog'):
    """Dispaly information about a pet"""
    print("\nI have a "+animal_typed+".")
    print("My "+animal_typed+"'s name is "+pet_name.title()+".")


describe_pet(pet_name="harry")
describe_pet(animal_typed='hamster', pet_name='harry')
