import { useState } from "react";
import {
  Container,
  Stack,
  Box,
  Center,
  Input,
  FormLabel,
  FormControl,
  Button,
  useDisclosure,
  Modal,
  ModalOverlay,
  ModalContent,
  ModalHeader,
  ModalFooter,
  ModalBody,
  ModalCloseButton,
} from "@chakra-ui/react";
import { useForm } from "react-hook-form";

function App() {
  const ModalToxico = ({ toxicidad }) => {
    console.log(toxicidad);
    let toxico;
    let color;
    if (toxicidad === 1) {
      toxico = "El nivel de toxicidad es bajo";
      color = "#97E673";
    } else if (toxicidad === 2) {
      toxico = "El nivel de toxicidad es Medio";
      color = "#E6DF7B";
    } else if (toxicidad === 0) {
      toxico = "El nivel de toxicidad es Alto";
      color = "#E67965";
    }
    return (
      <Modal isOpen={isOpen} onClose={onClose}>
        <ModalOverlay />
        <ModalContent bg={color}>
          <ModalHeader>Nivel de Toxicidad</ModalHeader>
          <ModalCloseButton />
          <ModalBody>{toxico}</ModalBody>

          <ModalFooter>
            <Button colorScheme="blue" mr={3} onClick={onClose}>
              Close
            </Button>
          </ModalFooter>
        </ModalContent>
      </Modal>
    );
  };

  const { isOpen, onOpen, onClose } = useDisclosure();
  const {
    register,
    handleSubmit,
    setValue,
    formState: { errors },
  } = useForm();
  const [toxicidad, setToxicidad] = useState(null);

  const onSubmit = handleSubmit(async (data) => {
    fetch("http://localhost:8000/data", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(data),
    }).then(async (data) => {
      if (data.ok) {
        const result = await data.json();
        setToxicidad(result.incidencia);
        onOpen();
      }
    });
  });

  return (
    <>
      <Box
        w={"100%"}
        h={"100vh"}
        display={"flex"}
        justifyContent={"center"}
        alignItems={"center"}
      >
        <FormControl w={"50%"} p={4} shadow={"xl"}>
          {toxicidad !== null ? (
            <ModalToxico toxicidad={toxicidad}></ModalToxico>
          ) : null}
          <form onSubmit={onSubmit}>
            <Center>
              <Stack w={"100%"} direction={["column", "row"]} spacing="24px">
                <Box w="30%">
                  <FormLabel>Total commits</FormLabel>
                  <Input
                    {...register("Total commits", {
                      required: true,
                    })}
                    variant="outline"
                    type="number"
                    step="any"
                  />
                </Box>
                <Box w="30%">
                  <FormLabel>Total commits per day</FormLabel>
                  <Input
                    {...register("Total commits per day", {
                      required: true,
                    })}
                    variant="outline"
                    type="number"
                    step="any"
                  />
                </Box>
                <Box w="30%">
                  <FormLabel>Accumulated commits</FormLabel>
                  <Input
                    {...register("Accumulated commits", {
                      required: true,
                    })}
                    variant="outline"
                    type="number"
                    step="any"
                  />
                </Box>
              </Stack>
            </Center>
            <Center mt={5}>
              <Stack w={"100%"} direction={["column", "row"]} spacing="24px">
                <Box w="30%">
                  <FormLabel>Committers</FormLabel>
                  <Input
                    {...register("Committers", {
                      required: true,
                    })}
                    variant="outline"
                    type="number"
                    step="any"
                  />
                </Box>
                <Box w="30%">
                  <FormLabel>Committers Weight</FormLabel>
                  <Input
                    {...register("Committers Weight", {
                      required: true,
                    })}
                    variant="outline"
                    type="number"
                    step="any"
                  />
                </Box>
              </Stack>
            </Center>
            <Center mt={5}>
              <Button type="submit"> Submit </Button>
            </Center>
          </form>
        </FormControl>
      </Box>
    </>
  );
}

export default App;
