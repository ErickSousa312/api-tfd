import { Request, Response } from 'express';
const Processo = require('../models/Processo')

class ProcessoController {
  async post(req: Request, res: Response): Promise<Response> {
    try {
      const response = await Processo.create(req.body);
      if (!response) {
        return res.status(400).json({ msg: "Erro ao criar Processos" });
      } else {
        return res.status(201).json({ msg: "Processos criado com sucesso", data: response });
      }
    } catch (error) {
      return res.status(400).json({ msg: 'Erro ao criar o Processos', error });
    }
  }

  async getByIdPaciente(req:Request, res:Response):Promise<Response>{
    try {
      const { id } = req.params;
      const response = await Processo.find({ idPaciente: id });
      if (!response) {
        return res.status(404).json({ msg: 'Processos não encontrado' });
      }
      return res.status(200).json({ msg: 'Processos médicos encontrado com sucesso', data: response });
    } catch (error) {
      return res.status(400).json({ msg: 'Erro ao buscar o Processos', error });
    }
  }

  async get(req: Request, res: Response): Promise<Response> {
    try {
      const { id } = req.params;
      const response = await Processo.findById(id);
      if (!response) {
        return res.status(404).json({ msg: 'Processos não encontrado' });
      }
      return res.status(200).json({ msg: 'Processos encontrado com sucesso', data: response });
    } catch (error) {
      return res.status(400).json({ msg: 'Erro ao buscar o Processos', error });
    }
  }

  async delete(req: Request, res: Response): Promise<Response> {
    try {
      const { id } = req.params;
      const response = await Processo.findOneAndDelete({ _id: id });
      if (!response) {
        return res.status(400).json({ msg: "Erro ao deletar o Parecer Medico" });
      } else {
        return res.status(200).json({ msg: "Parecer Medico deletado com sucesso", data: response });
      }
    } catch (error) {
      return res.status(400).json({ msg: "Erro ao deletar o Parecer Medico", error });
    }
  }

  async update(req: Request, res: Response): Promise<Response> {
    try {
      const { id } = req.params;
      const response = await Processo.findByIdAndUpdate(id, req.body, { new: true });
      if (!response) {
        return res.status(400).json({ msg: "Erro ao atualizar o Parecer Medico" });
      } else {
        return res.status(200).json({ msg: "Parecer Medico atualizado com sucesso", data: response });
      }
    } catch (error) {
      return res.status(400).json({ msg: "Erro ao atualizar o Parecer Medico", error });
    }
  }
}

export default ProcessoController;