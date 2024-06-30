
# Spirograph

The Spirograph is a tool for generating and visualizing spirograph patterns developed by [H. Kiani Moghaddam].

## Installation

1. Clone the repository:

```
git clone https://github.com/hkianim/spirograph.git
```

2. Navigate to the project directory:

```
cd spirograph
```

3. Create and activate a virtual environment:

   - On Windows:
     ```
     python -m venv .venv
     .venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```
     python3 -m venv .venv
     source .venv/bin/activate
     ```

4. Install the required dependencies:

```
pip install -r requirements.txt
```

## Usage

1. Run the main script:

```
python app.py
```

2. The application will open, and you can configure the spirograph parameters:
   - **Radius 1**: Set the radius of the outer circle.
   - **Radius 2**: Set the radius of the inner circle.
   - **Radius 3**: Set the distance of the pen from the center of the inner circle.
   - **Cycles**: Set the number of cycles the inner circle should rotate around the outer circle.

3. Click the "Render" button to generate the spirograph pattern.

## Contributing

If you would like to contribute to the development of this project, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them.
4. Push your changes to your forked repository.
5. Submit a pull request to the original repository.

We welcome all contributions, whether they are bug fixes, new features, or improvements to the existing code.

## License

This project is licensed under the [MIT License](LICENSE).
