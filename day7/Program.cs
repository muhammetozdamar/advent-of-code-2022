using System;
using System.Collections.Generic;

namespace day7
{
    class Program
    {
        static void Main(string[] args)
        {
            string[] lines = System.IO.File.ReadAllLines(@"input.txt");

            Directory currentDirectory = null;
            List<Directory> directories = new List<Directory>();

            for (int i = 0; i < lines.Length; i++)
            {
                if (lines[i].Trim().Length == 0) continue;
                string[] lineParts = lines[i].Split(" ");
                if (lineParts[0] == "$") // This is command line cd/ls
                {
                    if (lineParts[1] == "cd") // Change directory, create if needed
                    {
                        string directoryName = lineParts[2];
                        if (directoryName == "..")
                        {
                            currentDirectory = currentDirectory.parent;
                        }
                        else
                        {
                            Directory dir = directories.Find((directory) => directory.name == directoryName && directory.parent == currentDirectory);
                            if (dir == null)
                            {
                                dir = new Directory(currentDirectory, directoryName);
                                directories.Add(dir);
                            }
                            currentDirectory = dir;
                        }
                    }
                }
                else
                {
                    FileSystemObject obj;
                    if (lineParts[0] == "dir")
                    {
                        string directoryName = lineParts[1];
                        obj = directories.Find((directory) => directory.name == directoryName && directory.parent == currentDirectory);
                        if (obj == null)
                        {
                            obj = new Directory(currentDirectory, directoryName);
                            directories.Add(obj as Directory);
                        }
                    }
                    else
                    {
                        long fileSize = long.Parse(lineParts[0]);
                        string fileName = lineParts[1];
                        obj = new File(currentDirectory, fileName, fileSize);
                    }
                    currentDirectory.AddChild(obj);
                }
            }

            long totalSize = 0;
            long smallestBigEnoughtFileSize = long.MaxValue;
            long neededSize = 30000000 - (70000000 - directories[0].GetSize());
            foreach (Directory dir in directories)
            {
                long size = dir.GetSize();
                if (size <= 100000)
                {
                    totalSize += size;
                }
                if (size >= neededSize && smallestBigEnoughtFileSize >= size)
                {
                    smallestBigEnoughtFileSize = size;
                }
            }
            Console.WriteLine("Total Size: " + totalSize);
            Console.WriteLine("Smallest Big Enough To Clear Size: " + smallestBigEnoughtFileSize);
        }
    }

    abstract class FileSystemObject
    {
        public string name;
        public Directory parent;
        public abstract long GetSize();
    }

    class Directory : FileSystemObject
    {
        public List<FileSystemObject> children;

        public Directory(Directory parent, string name)
        {
            this.name = name;
            this.parent = parent;
            children = new List<FileSystemObject>();
        }

        public void AddChild(FileSystemObject obj)
        {
            if (obj == this) return;
            FileSystemObject existing = children.Find((child) => child.name == obj.name && child.parent == parent);
            if (existing != null && existing.GetType() == obj.GetType()) return;
            children.Add(obj);
        }
        public override long GetSize()
        {
            long size = 0;
            foreach (FileSystemObject child in children)
            {
                if (child == this)
                {
                    continue;
                }
                size += child.GetSize();
            }
            return size;
        }
    }

    class File : FileSystemObject
    {
        public long size;
        public File(Directory parent, string name, long size)
        {
            this.name = name;
            this.size = size;
            this.parent = parent;
        }

        public override long GetSize()
        {
            return size;
        }
    }
}