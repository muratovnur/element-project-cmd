import os
from constants import FILE_NOT_FOUND_MESSAGE, FILE_ALREADY_EXISTS_MESSAGE

currentPath = "C:\\"
os.chdir(currentPath)

print('Terminal is running! Type "help" for a list of available commands.')
print('WARNING! Directory names with white spaces are currently unreachable. It is recommended to type file/folder names exactly as they are.')
print(os.getcwd(), '>', sep='', end='')

while True:
  cmd = input().split(' ')

  match cmd[0]:
    case 'dir':
      dirList = os.listdir(currentPath)
      if len(dirList) == 0:
        print('Directory is empty.')
      for dir in dirList:
        if os.path.isdir(f'{currentPath}\\{dir}'):
          print(f'[dir]:  {dir}', sep='\n')
        else:
          print(f'[file]: {dir}', sep='\n')

    case 'cd':
      if cmd[1] != '..':
        try:
          if not os.path.isdir(f'{currentPath}\\{cmd[1]}'):
            raise FileNotFoundError(f'[{cmd[1]}]: {FILE_NOT_FOUND_MESSAGE}')

          currentPath += f'\\{cmd[1]}'
          os.chdir(f'{currentPath}')

        except FileNotFoundError as error:
          print(error)
          
      else:
        currentPath = currentPath.replace(f'\\{os.path.basename(currentPath)}', '')
        os.chdir(f'{currentPath}')

    case 'touch':
      try:
        if os.path.isfile(f'{currentPath}\\{cmd[1]}'):
          raise FileExistsError(f'[{cmd[1]}]: {FILE_ALREADY_EXISTS_MESSAGE}')

        with open(f'{currentPath}\\{cmd[1]}', 'x') as file:
          pass
        print(f'{cmd[1]} file created successfully!')

      except (FileExistsError, OSError) as error:
        print(error)
    
    case 'del':
      try:
        if not os.path.isfile(f'{currentPath}\\{cmd[1]}'):
          raise FileNotFoundError(f'[{cmd[1]}]: {FILE_NOT_FOUND_MESSAGE}')

        os.remove(f'{currentPath}\\{cmd[1]}')
        print(f'{cmd[1]} file deleted successfully!')

      except FileNotFoundError as error:
        print(error)

    case 'mkdir':
      try:
        if os.path.isdir(f'{currentPath}\\{cmd[1]}'):
          raise FileExistsError(f'[{cmd[1]}]: {FILE_ALREADY_EXISTS_MESSAGE}')

        os.mkdir(f'{currentPath}\\{cmd[1]}')
        print(f'{cmd[1]} directory created successfully!')

      except (FileExistsError, OSError) as error:
        print(error)
    
    case 'rmdir':
      try:
        if not os.path.isdir(f'{currentPath}\\{cmd[1]}'):
          raise FileNotFoundError(f'[{cmd[1]}]: {FILE_NOT_FOUND_MESSAGE}')

        os.rmdir(f'{currentPath}\\{cmd[1]}')
        print(f'{cmd[1]} directory deleted successfully!')

      except FileNotFoundError as error:
        print(error)

    case 'rename':
      try:
        if not os.path.isdir(f'{currentPath}\\{cmd[1]}') and not os.path.isfile(f'{currentPath}\\{cmd[1]}'):
          raise FileNotFoundError(f'[{cmd[1]}]: {FILE_NOT_FOUND_MESSAGE}')

        if os.path.isdir(f'{currentPath}\\{cmd[2]}') and os.path.isfile(f'{currentPath}\\{cmd[2]}'):
          raise FileExistsError(f'[{cmd[1]}]: {FILE_ALREADY_EXISTS_MESSAGE}')

        os.rename(f'{cmd[1]}', f'{cmd[2]}')
        print(f'{cmd[1]} directory renamed to {cmd[2]} successfully!')

      except (FileNotFoundError, FileExistsError) as error:
        print(error)

    case 'read':
      try:
        if not os.path.isfile(f'{currentPath}\\{cmd[1]}'):
          raise FileNotFoundError(f'[{cmd[1]}]: {FILE_NOT_FOUND_MESSAGE}')

        with open(f'{currentPath}\\{cmd[1]}', 'r') as file:
          print(file.read())

      except FileNotFoundError as error:
        print(error)

    case 'help':
      print('''Available commands:
      cd [path]: Change current directory.
      dir: List all files and folders of a current directory. 
      mkdir [name]: Create a folder in a current directory.
      rmdir [name]: Delete a folder in a current directory.
      touch [name]: Create a file in a current directory.
      del [name]: Delete a file in a current directory.
      rename [name] [new_name]: Rename a file or a folder.
      read [name]: Read a file.
      help: Show available commands.
      ''')

    case 'exit':
      break

    case _:
      print(f'[{cmd[0]}] is not a command. Type "help" for a list of available commands.')

  print(f'{currentPath}>', end='')
  