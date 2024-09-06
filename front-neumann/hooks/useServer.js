import server from "../server/server";
import { useMutation } from "@tanstack/react-query";

async function fetchServer() {
    const res = await server.get().then((res) => {
        return res.data;
    }).catch((e) => {
        return e;
    });
    return res
}

export const useServer = () => {
    return useMutation({
        mutationFn: fetchServer,
    })
}