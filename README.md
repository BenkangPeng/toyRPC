# toyRPC 🚀

A minimalist cross-language RPC framework supporting Python <-> C++ interoperability.

## Features ✨
- Simple method registration using decorators
- Cross-language method calls (Python ↔ C++)
- Dynamic proxy client with magic method dispatch
- Singleton server implementation
- Built-in calculator and system monitoring examples
- Matrix operations via C++ optimizations

## Tech Stack ⚙️
- **Python**: Core RPC implementation
- **C++**: High-performance computing functions
- **Cython**: Python-C++ interoperability
- **Java**: Experimental implementation (WIP)

## Installation 📦
```bash
git clone https://github.com/BenkangPeng/toyRPC.git
cd toyRPC
pip install -r requirements.txt

# For C++ extensions
cd src/cc
python setup.py build_ext --inplace
```

## Usage 🛠️

### Python Provider-Consumer Example

**Provider** (`tests/example-provider-consumer/provider.py`):

* Open a terminal, run the `provider.py`

  ```shell
  python provider.py
  ```

The server is listening to all the ports.

**Consumer** (`tests/example-provider-consumer/consumer.py`):

* Open another terminal(or another device under the same LAN(local area network):

  ```shell
  python consumer.py
  ```

## Project Structure 📂

```plainText
toyRPC/
├── src/
│   ├── cc/              # C++ implementations
│   └── python/          # Core RPC implementation
│       ├── client.py    # RPC client
│       ├── server.py    # RPC server
│       └── register*    # Registration decorators
├── tests/               # Example implementations
└── requirements.txt     # Python dependencies
```

## TroubleShooting ❓

Make sure adding the folder `src`'s location(`/path/to/project/src`) into the `$PYTHONPATH` if encounted the errors of packages importing.

If use `VSCode` as IDE, you can add it in `.vscode/settings.json`.

```json
{
  "terminal.integrated.env.windows": {
    "PYTHONPATH": "${workspaceFolder}\\src;${env:PYTHONPATH}"
  }
}
```



## Contributing 🤝

Contributions welcome! Please open an issue first to discuss proposed changes.

## License 📄

Apache 2.0 - See [LICENSE](https://file+.vscode-resource.vscode-cdn.net/c%3A/Users/benka/.vscode/extensions/marscode.marscode-extension-1.2.16/LICENSE) for details.
