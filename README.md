# ToElement

## Synopsis

演示代码或是只是打开看的时候，可能会不小心键入一些字母进去。为了解决误入问题，编写了一个只读/编辑模式切换工具。

## Code Example

可以设置默认参数
```json
{
	"readonly_default" : true,	// 打开文件是否默认只读
	"deactivated_lock" : false 	// 文件失去焦点是否自动锁定只读
}
```

可以自行配置快捷键
```json
{ "keys": ["command+i"], "command": "set_writable" },
{ "keys": ["command+e"], "command": "set_writable" },
{ "keys": ["command+shift+i"], "command": "set_readonly" },
{ "keys": ["command+shift+e"], "command": "set_readonly" },
```

## License

MIT, Apache, etc.
