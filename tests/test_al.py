from al.al import main


def test_main_output(capsys):
    # Call the main function
    main()

    # Capture the output
    captured = capsys.readouterr()

    # Assert the output is as expected
    assert captured.out == "hey there, I am AL!\n"
