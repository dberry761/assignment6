class EmployeeNode:
    '''
    A class to represent a node in the binary tree.
    Attributes:
        name (str): The name of the employee.
        left (EmployeeNode): The left child node, representing the left subordinate.
        right (EmployeeNode): The right child node, representing the right subordinate.
    '''
    def __init__(self, name):
        self.name = name
        self.left = None
        self.right = None


class TeamTree:
    '''
    A class to represent a binary tree for managing a team structure.
    Attributes:
        root (EmployeeNode): The root node of the tree, representing the team lead.
    Methods:
        insert(manager_name, employee_name, side, current_node=None): Inserts a new employee under the specified manager.
        print_tree(node=None, level=0): Prints the tree structure starting from the given node.

    '''
    def __init__(self):
        self.root = None

    def print_tree(self, node=None, level=0):
        if node is None:
            node = self.root
        if node is None:
            return
        indent = '    ' * level
        print(f"{indent}- {node.name}")
        if node.left:
            self.print_tree(node.left, level + 1)
        if node.right:
            self.print_tree(node.right, level + 1)

    def insert(self, manager_name, employee_name, side, current_node=None):
        '''
        Inserts a new employee under the specified manager.
        Args:
            manager_name (str): The name of the manager under whom to add the new employee.
            employee_name (str): The name of the new employee to add.
            side (str): 'left' or 'right' indicating where to add the new employee.
            current_node (EmployeeNode): The current node being checked (used for recursion).
        '''
        if self.root is None:
            print("⚠️ The team lead must be added first.")
            return

        if current_node is None:
            current_node = self.root

        if current_node.name == manager_name:
            new_employee = EmployeeNode(employee_name)
            if side == 'left':
                if current_node.left is None:
                    current_node.left = new_employee
                    print(f"✅ {employee_name} added as left subordinate of {manager_name}.")
                else:
                    print(f"❌ Left subordinate already exists for {manager_name}.")
            elif side == 'right':
                if current_node.right is None:
                    current_node.right = new_employee
                    print(f"✅ {employee_name} added as right subordinate of {manager_name}.")
                else:
                    print(f"❌ Right subordinate already exists for {manager_name}.")
            else:
                print("❌ Side must be 'left' or 'right'.")
            return

        if current_node.left:
            self.insert(manager_name, employee_name, side, current_node.left)
        if current_node.right:
            self.insert(manager_name, employee_name, side, current_node.right)

# Test your code here

if __name__ == "__main__":
    test_tree = TeamTree()
    test_tree.root = EmployeeNode("CEO")

    test_tree.insert("CEO", "Manager1", "left")
    test_tree.insert("CEO", "Manager2", "right")
    test_tree.insert("Manager1", "EmployeeA", "left")

    print("\nTest Tree Output:")
    test_tree.print_tree()








# CLI functionality
def company_directory():
    tree = TeamTree()

    while True:
        print("\n📋 Team Management Menu")
        print("1. Add Team Lead (root)")
        print("2. Add Employee")
        print("3. Print Team Structure")
        print("4. Exit")
        choice = input("Choose an option (1–4): ")

        if choice == "1":
            if tree.root:
                print("⚠️ Team lead already exists.")
            else:
                name = input("Enter team lead's name: ")
                tree.root = EmployeeNode(name)
                print(f"✅ {name} added as the team lead.")

        elif choice == "2":
            manager = input("Enter the manager's name: ")
            employee = input("Enter the new employee's name: ")
            side = input("Should this employee be on the LEFT or RIGHT of the manager? ")
            side = side.lower()
            tree.insert(manager, employee, side)

        elif choice == "3":
            print("\n🌳  Current Team Structure:")
            tree.print_tree()

        elif choice == "4":
            print("Good Bye!")
            break
        else:
            print("❌ Invalid option. Try again.")


if __name__ == "__main__":
    test_tree = TeamTree()
    test_tree.root = EmployeeNode("CEO")

    test_tree.insert("CEO", "Manager1", "left")
    test_tree.insert("CEO", "Manager2", "right")
    test_tree.insert("Manager1", "EmployeeA", "left")

    print("\nTest Tree Output:")
    test_tree.print_tree()

    company_directory()