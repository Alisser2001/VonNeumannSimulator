import server from "../server/server";
import { useMutation } from "@tanstack/react-query";

async function fetchServer(x, y) {
    const res = await server.get(`/?x=${x}&y=${y}`).then((res) => {
        return res.data;
    }).catch((e) => {
        return e;
    });
    return res
}

export const useServer = () => {
    return useMutation({
        mutationFn: ({x, y}) => fetchServer(x, y),
    })
}