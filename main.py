class Solution:
    def simplifyPath(self, path: str) -> str:
        directories = path.split('/')
        stack = []

        for directory in directories:
            # remove the last directory from your path (if there is one), as '..' refers to moving one directory up.
            if directory == '..':
                if stack:
                    stack.pop()

            # Skip it if it's an empty string or '.', as these refer to the current directory.        
            elif directory and directory != '.':
                stack.append(directory)

        # Join the processed parts with '/' to form the simplified path.
        simplified_path = '/' + '/'.join(stack)
        return simplified_path              
   
